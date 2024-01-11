import gradio as gr
import openai
import os
import random

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')
print(openai.api_key)
print (os.environ.get("OPENAI_API_KEY"))
client = openai.OpenAI(organization='org-eiNl8e4nk93VLQFDb4EBz9JG')
#openai.api_key = os.environ['openai']  #for huggingface i think

#generates an AI description of your character
def describe(names,wis,char,str,int,dex,con):
    print(f"hi{names}")
    
    prom=f"We're generating Dungeons and Dragons characters for a new campaign, and we need a brief character description, including race"
    prom+=f" and class. The character's name is {names} with the following stats: Wisdom: {wis},Charisma:{char},Strength:{str},"
    prom+=f"Intelligence:{int},Dexterity:{dex},Constitution:{con}. Describe the character, and then, separated by $$$ give us the "
    prom+=f"character's interesting backstory."

    completion = client.completions.create(
		model='gpt-3.5-turbo-instruct',
		prompt=prom,
		max_tokens=510,
		temperature=0.77,
		frequency_penalty=0.2,
		presence_penalty= 0.25)

    result =completion.choices[0].text
	#print(dict(completion).get('usage'))


	#print(completion.model_dump_json(indent=2))

    if not result :
        result = "Could you be any more boring?"
        

    return result
        
    

iface = gr.Interface(fn=describe, inputs=[gr.Textbox(label="Your DND character",show_label=True),
                                    gr.Number(label="Wisdom",show_label=True), 
                                    gr.Number(label="Charisma",show_label=True), 
                                    gr.Number(label="Strength",show_label=True), 
                                    gr.Number(label="Intelligence",show_label=True), 
                                    gr.Number(label="Dexterity",show_label=True), 
                                    gr.Number(label="Constitution",show_label=True)], 

            outputs=gr.Textbox(label="The character",show_label=True))
iface.launch()


def stat(n_dice, dice_rank):
    results = [  # Generate n_dice numbers between [1,dice_rank]
        random.randint(1, dice_rank)
        for n
        in range(n_dice)
    ]
    lowest = min(results)  # Find the lowest roll among the results
    results.remove(lowest)  # Remove the first instance of that lowest roll
    return sum(results)  # Return the sum of the remaining results.