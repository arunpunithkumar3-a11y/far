import pickle
import pandas as pd
import numpy as np
model1 = pickle.load(open("crop.pkl","rb"))
model2 = pickle.load(open("growth.pkl","rb"))
model3 = pickle.load(open("yelid.pkl","rb"))
model4 = pickle.load(open("water.pkl","rb"))
model5 = pickle.load(open("ph.pkl","rb"))
model6 = pickle.load(open("fert.pkl","rb"))
model7 = pickle.load(open("remark.pkl","rb"))
model8 = pickle.load(open("health.pkl","rb"))
el1 = pickle.load(open("crop_el.pkl","rb"))
el2 = pickle.load(open("fert_el1.pkl","rb"))
el3 = pickle.load(open("fert_el2.pkl","rb"))
el4 = pickle.load(open("health_el.pkl","rb"))

def predict_output(user_input:dict):
    input_df = pd.DataFrame([user_input])
    probs = model1.predict_proba(input_df)[0]
    classes = model1.named_steps['xg'].classes_

    
    top5_idx = np.argsort(probs)[::-1][:5]
    decode = el1.inverse_transform(classes)
    top =[decode[i] for i in top5_idx]
    response=[]


    for x in top:
        input_i = {"crops": x}
        input_i.update(user_input)
        out = pd.DataFrame([input_i])
        growth_days = model2.predict(out)
        yield_per = model3.predict(out)
        water_req = model4.predict(out)
        ph = model5.predict(out)

        response.append({
        "crop": x,
        "growth_days": float(growth_days[0]),
        "yield_per_hectare": float(yield_per[0]),
        "water_required": float(water_req[0]),
        "ideal_ph": float(ph[0])
    })
    return response
def predict_outpu1(user:dict):
    input_df1 = pd.DataFrame([user]) 
    probs1 = model6.predict_proba(input_df1)[0]
    probs2 = model7.predict_proba(input_df1)[0]
    classes1= model6.named_steps['xg'].classes_ 
    classes2 = model7.named_steps["xg1"].classes_
    top5_idx1 = np.argsort(probs1)[::-1][:5]
    top5_idx2 = np.argsort(probs2)[::-1][:5]
    decode = el2.inverse_transform(classes1)
    decode2 = el3.inverse_transform(classes2)
    top1 =[decode[i] for i in top5_idx1]
    top2 =[decode2[i] for i in top5_idx2]
    response1 = []

    for fe, re in zip(top1, top2):
        response1.append({
        "fert": fe,
        "remark": re
        })
    return response1
def predict_output3(user1:dict):
    input_df2 = pd.DataFrame([user1])
    pre = model8.predict(input_df2)
    decode3 = el4.inverse_transform(pre)
    return decode3
