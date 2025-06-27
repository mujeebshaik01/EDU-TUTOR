from ibm_watson_machine_learning.foundation_models import Model
from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams

class WatsonxClient:
    def __init__(self):
        self.credentials = {
            "url": "https://us-south.ml.cloud.ibm.com",
            "apikey": "YOUR_API_KEY"
        }
        self.project_id = "YOUR_PROJECT_ID"
        
    def generate_diagnostic_test(self, grade_level, subjects):
        model = Model(
            model_id="meta-llama/llama-2-70b-chat",
            credentials=self.credentials,
            project_id=self.project_id
        )
        
        prompt = f"""
        Create a diagnostic test for a {grade_level} student covering {subjects}.
        Include questions that assess foundational knowledge and critical thinking.
        """
        
        parameters = {
            GenParams.DECODING_METHOD: "sample",
            GenParams.MAX_NEW_TOKENS: 1000,
            GenParams.TEMPERATURE: 0.7
        }
        
        return model.generate_text(prompt, parameters)