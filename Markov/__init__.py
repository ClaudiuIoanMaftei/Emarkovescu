import markovify

model=None

def create_model(poems,state_size=2):
    global model

    for poem in poems:
        copy=model
        try:
            local_model = markovify.Text(poem,state_size)
            if model == None:
                model = local_model
            else:
                model=markovify.combine([model,local_model])
        except:
            model=copy

    with open("model.json","w") as f:
        f.write(model.to_json())

def load_model():
    global model

    with open("model.json", "r") as f:
        data=f.read()
        model=markovify.Text.from_json(data)
        model.compile()