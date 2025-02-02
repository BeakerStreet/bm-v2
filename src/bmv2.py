import tensorflow as tf
import sagemaker
from pydantic import BaseModel
from openai import OpenAI

class bmv2:
    def __init__(self, bucket):
        self.role = self.get_role()
        self.bucket = bucket
        self.model = None
    
    def get_role(self):
        return sagemaker.get_execution_role()


        completion = self.client.beta.chat.completions.parse(
            model="gpt-4o-2024-08-06",
            messages=[
                {"role": "system", "content": self.prompts[0]},
                {"role": "user", "content": self.prompts[1]},
            ],
            response_format=Behaviours,
        )

        event = completion.choices[0].message.parsed

        self.behaviours = event # this is probably incorrectly formatted

        return event
    
    def get_prompts(self) -> list[str]:
        '''
        OpenAI prompt to convert .json dataset
        of build order data to structured 
        behaviours insights
        '''
    
        system_prompt = "" # replace with system prompt
        user_prompt = "" # replace with user prompt

        return [system_prompt, user_prompt]

class Behaviours(BaseModel):
    '''
    Pydantic model for behaviour data
    '''

    def __init__(self):
        
        self.pseudo_yields = {
            "PSEUDOYIELD_UNIT_SETTLER": float,
            "PSEUDOYIELD_CITY_BASE": float,
            "PSEUDOYIELD_UNIT_EXPLORER": float,
            "PSEUDOYIELD_CLEAR_BANDIT_CAMPS": float,
            "PSEUDOYIELD_TECHNOLOGY": float,
            "PSEUDOYIELD_CIVIC": float,
        }
        
        self.default_yield_bias = {
            "YIELD_PRODUCTION": float,
            "YIELD_SCIENCE": float,
            "YIELD_GOLD": float,
            "YIELD_FAITH": float,
        }


        completion = self.client.beta.chat.completions.parse(
            model="gpt-4o-2024-08-06",
            messages=[
                {"role": "system", "content": self.prompts[0]},
                {"role": "user", "content": self.prompts[1]},
            ],
            response_format=Behaviours,
        )

        event = completion.choices[0].message.parsed

        self.behaviours = event # this is probably incorrectly formatted

        return event
    
    def get_prompts(self) -> list[str]:
        '''
        OpenAI prompt to convert .json dataset
        of build order data to structured 
        behaviours insights
        '''
    
        system_prompt = "" # replace with system prompt
        user_prompt = "" # replace with user prompt

        return [system_prompt, user_prompt]


class Behaviours(BaseModel):
    '''
    Pydantic model for behaviour data
    '''

    def __init__(self):
        
        self.pseudo_yields = {
            "PSEUDOYIELD_UNIT_SETTLER": float,
            "PSEUDOYIELD_CITY_BASE": float,
            "PSEUDOYIELD_UNIT_EXPLORER": float,
            "PSEUDOYIELD_CLEAR_BANDIT_CAMPS": float,
            "PSEUDOYIELD_TECHNOLOGY": float,
            "PSEUDOYIELD_CIVIC": float,
        }
        
        self.default_yield_bias = {
            "YIELD_PRODUCTION": float,
            "YIELD_SCIENCE": float,
            "YIELD_GOLD": float,
            "YIELD_FAITH": float,
        }
