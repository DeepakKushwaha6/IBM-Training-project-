import streamlit as st
from PIL import Image

from predict import predict_image

st.title("Cat vs Dog Classifier")

uploaded_file = st.file_uploader(
    "Upload an Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(
        uploaded_file
    )

    st.image(
        image,
        caption="Uploaded Image",
        use_container_width=True
    )

    prediction, confidence = predict_image(
        image
    )

    # Reject unknown images
    if confidence < 90:

        st.warning(
            "Model is not trained for this image"
        )

        st.write(
            f"Confidence: {confidence:.2f}%"
        )

    else:

        st.success(
            f"Prediction: {prediction}"
        )

        st.write(
            f"Confidence: {confidence:.2f}%"
        )

