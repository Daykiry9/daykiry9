import pandas as pd

# Carga tu archivo CSV (ajusta la ruta según corresponda)
df = pd.read_csv("Empresas_con_pais.csv")

# Asegúrate de que la columna con empresas se llama 'Company'
df = df.rename(columns={'CRM_Account': 'Company'})  # solo si aplica

# Paso 1: Extraer nombres únicos
empresas = df['Company'].dropna().unique()

# Paso 2: Construcción manual del diccionario
# Completado con datos verificados:
country_map = {
    "Alliance Laundry Systems LLC": "Estados Unidos",
    "Speed Queen": "Estados Unidos",
    "EMBRAER S.A.": "Brasil",
    # Añade el resto de tus empresas aquí
}

# Paso 3: Usar el diccionario para mapear los países
df['PaísOrigen'] = df['Company'].map(country_map)

# (Opcional) Mostrar las que no se pudieron mapear para que las completes
faltantes = df[df['PaísOrigen'].isnull()]['Company'].unique()
print("Faltantes por mapear:", faltantes)

# Paso 4: Guardar el archivo final
df.to_csv("Empresas_completadas.csv", index=False)
