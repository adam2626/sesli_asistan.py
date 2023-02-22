import pickle

# Model eğitimi
...

# Eğitilmiş modelin kaydedilmesi
with open('model.pkl', 'wb') as dosya:
    pickle.dump(model, dosya)
