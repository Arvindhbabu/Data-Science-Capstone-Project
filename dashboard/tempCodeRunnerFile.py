X_columns = model.feature_names_in_  # Ensure matching order
# Add missing columns and ensure correct order
for col in X_columns:
    if col not in input_encoded.columns:
        input_encoded[col] = 0
input_encoded = input_encoded[X_columns]
input_scaled = scaler.transform(input_encoded)
