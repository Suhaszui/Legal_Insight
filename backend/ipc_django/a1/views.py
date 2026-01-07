from django.shortcuts import render
from a1 import ipc_explanations

import joblib
def home(request):
    # Default view state
    context = {
        'view': 'about', # Can be 'about', 'predictor', or 'result'
    }
    pipeline = joblib.load(r'C:\legal_ai_project\ipc_model\models\ipc_pipeline.joblib')
    if request.method == 'POST':
        # Check which button was clicked
        action = request.POST.get('action')
        
        if action == 'go_to_predictor':
            context['view'] = 'predictor'
            
        elif action == 'predict':
            facts = request.POST.get('case_facts', '')
            # Logic: Here you would call your ML model. 
            # For now, we simulate a result.
            context['view'] = 'result'
            context['facts'] = facts
            prediction=pipeline.predict([facts])
            context['prediction'] = prediction[0]
            reason = ipc_explanations.EXPLANATIONS.get(prediction[0], "Prediction based on patterns learned from case data.")


            context['reason'] = reason

    return render(request, 'a1/a1.html', context)