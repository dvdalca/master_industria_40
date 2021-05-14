import tenserflow

model = tk.keras.applications.MobilenteV2()

result = model.predict(image)

print(result)
