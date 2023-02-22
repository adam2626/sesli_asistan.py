import pickle

# Model eğitimi
...

# Eğitilmiş modelin kaydedilmesi
with open('model.pk1', 'wb') as dosya:
    pickle.dump(model, dosya)
