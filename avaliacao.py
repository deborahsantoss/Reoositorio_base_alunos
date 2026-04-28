import streamlit as st

st.title("Calculadora IMC 📱")
st.subheader("Feito com Streamlit ❤️")

altura = st.number_input("Digite a sua altura", min_value=0.0)
peso = st.number_input("Digite o seu peso", min_value=0.0)

if st.button("Calcular"):
    imc = peso / altura** 2 
    
    if imc < 18.5:
        st.image()
        st.error("Abaixo do peso ☠️") 


    elif imc < 24.9:
        st.image("https://conteudo.imguol.com.br/c/splash/b0/2022/03/12/camila-loures-posa-em-frente-a-sua-nova-mansao-em-sao-paulo-1647126206074_v2_900x506.jpg")
        st.error("Peso normal")

    elif imc < 29.9:
        st.image("https://static.wikia.nocookie.net/hero2/images/7/7c/HomerSimpson.webp/revision/latest?cb=20231213233714&path-prefix=es")
        st.error("Sobrepeso") 

    elif imc < 34.9:
        st.image("https://static1.purepeople.com.br/articles/5/38/57/45/@/4430710-jojo-todynho-vive-uma-nova-fase-na-vida-1200x0-2.jpg")
        st.error("Obesidade I")

    elif imc < 39.9:
        st.image("https://i.pinimg.com/originals/15/81/0b/15810b66d27f5470566a1c22aa300d8d.jpg)
        st.error("Obesidade II")

    else:
        st.image("https://img.lovepik.com/png/20231111/fat-clipart-an-obese-happy-cartoon-character-vector-obesity-happy_559816_wh1200.png)
        st.error("Obesidade III")
