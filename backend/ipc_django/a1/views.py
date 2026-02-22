from django.shortcuts import render
import joblib
from pathlib import Path
from a1.ipc_explanations import EXPLANATIONS

# --- SAFE PATH FOR LOCAL + RENDER ---
BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "ipc_model" / "models" / "ipc_pipeline.joblib"

# Load once (BEST PRACTICE)
pipeline = joblib.load(MODEL_PATH)


def home(request):
    context = {
        'view': 'about',
    }

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'go_to_predictor':
            context['view'] = 'predictor'

        elif action == 'predict':
            facts = request.POST.get('case_facts', '')
            context['view'] = 'result'
            context['facts'] = facts

            prediction_array = pipeline.predict([facts])
            result_label = prediction_array[0]

            context['prediction'] = result_label

            reason = EXPLANATIONS.get(
                result_label,
                "Prediction based on patterns learned from case data."
            )
            context['reason'] = reason

    return render(request, 'a1/a1.html', context)