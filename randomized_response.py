import numpy as np
import pandas as pd
import copy
import random
from IPython.display import display
import matplotlib.pyplot as plt

%matplotlib inline

protected_attrs = {
    'gender' : ['male','female'],
    'country' : ['brazil','swtitzerland','other'],
    'age' : (18,40)
}

survey = {
    'HIV_positive' : ['yes','no']
}

def generate_dataset(n):
    dataset = []
    for i in range(n):
        protected_sample = [v[random.randint(0,len(v)-1)] if type(v) is list else random.randint(v[0],v[1]) for k,v in protected_attrs.items()]
        survey_sample = [v[1] if (random.uniform(0,1)>=0.0038) else v[0] for k,v in survey.items()]
        sample = protected_sample + survey_sample
        dataset.append(sample)
        
    columns = list(protected_attrs.keys()) + list(survey.keys()) 
    return pd.DataFrame(dataset,columns=columns)

#small_dataset = generate_dataset(500)
big_dataset = generate_dataset(5000)

display(big_dataset)

count = 0
for i in range(0,5000):
    if(big_dataset.HIV_positive[i] is 'yes'):
        count=count+1
print(count)

def synthetic_dataset(n):
    synth_dataset = big_dataset.drop('HIV_positive',axis=1)
    synth_dataset['HIV_positive'] = ''
    dt = []
    
    lancamentos = []
    
    for i in range(n):
        primeiro_lancamento = random.uniform(0,1)
        segundo_lancamento = random.uniform(0,1)
        
        #lancamentos.append(primeiro_lancamento) 
        #lancamentos.append(segundo_lancamento)
        
        #sample2 = [big_dataset.HIV_positive[i] if (primeiro_lancamento<=0.5) else (v[0] if(segundo_lancamento < 0.5*0.05) else v[1]) for k,v in survey.items()]
        sample2 = [big_dataset.HIV_positive[i] if (primeiro_lancamento<=0.5) else (v[0] if(segundo_lancamento < 0.0038) else v[1]) for k,v in survey.items()]
        dt.append(sample2)
    dt = np.reshape(dt, (-1))
    synth_dataset.HIV_positive = dt
    #print(type(synth_dataset.HIV_positive))
    return pd.DataFrame(synth_dataset)

st = synthetic_dataset(5000)
#print(type(st))

display(st)

plt.plot(st.HIV_positive)
plt.plot(big_dataset.HIV_positive)

print(st["HIV_positive"].value_counts()) 