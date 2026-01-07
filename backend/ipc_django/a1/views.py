from django.shortcuts import render
import joblib
from a1.ipc_explanations import EXPLANATIONS
def home(request):
    # Default view state
    context = {
        'view': 'about', # Can be 'about', 'predictor', or 'result'
    }
    pipeline = joblib.load(r'C:\legal_ai_project\ipc_model\models\ipc_pipeline.joblib')
    if request.method == 'POST':
        action = request.POST.get('action')
        
        if action == 'go_to_predictor':
            context['view'] = 'predictor'
            
        elif action == 'predict':
            facts = request.POST.get('case_facts', '')
            context['view'] = 'result'
            context['facts'] = facts
            
            # This returns an array like: array(['IPC 302'], dtype=object)
            prediction_array = pipeline.predict([facts])
            
            # FIX: Extract the first element from the array to get the string "IPC 302"
            result_label = prediction_array[0] 
            
            context['prediction'] = result_label
            
            # Now result_label is a string, which is hashable!
            reason = EXPLANATIONS.get(result_label, "Prediction based on patterns learned from case data.")
            context['reason'] = reason

    return render(request, 'a1/a1.html', context)