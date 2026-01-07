import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report, accuracy_score,confusion_matrix,f1_score
import joblib
from sklearn.pipeline import Pipeline

df = pd.read_csv(r'C:\legal_ai_project\ipc_model\data\processed\processed.csv')


X = df['facts']
y = df['ipc_section']

vc=y.value_counts()
less_count=vc[vc==1]
df.drop(df[df['ipc_section'].isin(less_count.index)].index, inplace=True)


X = df['facts']
y = df['ipc_section']

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    stratify=y,
    random_state=69
)

vectorizer = TfidfVectorizer(
    max_features=5000,
    stop_words='english',
    ngram_range=(1,2),

)

X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

model_svc = LinearSVC(
    random_state=42,
    max_iter=1000,
    class_weight='balanced',
  
)


model_svc.fit(X_train_tfidf, y_train)

pipeline=Pipeline([
                ('vectorizer',vectorizer),
                ('svm',model_svc)
          ])
joblib.dump(pipeline,r'C:\legal_ai_project\ipc_model\models\ipc_pipeline.joblib')