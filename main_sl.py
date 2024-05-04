import streamlit as st
from rembg import remove
from PIL import Image
import io


# def remove_background(input_image):
#     # Removing the background from the given image
#     output_image = remove(input_image)
#     return output_image

# def main():
#     st.title("Background Remover")

#     uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

#     if uploaded_file is not None:
#         # Display uploaded image
#         input_image = Image.open(uploaded_file)
#         st.image(input_image, caption="Uploaded Image", use_column_width=True)

#         # Process the image and remove background
#         output_image = remove_background(input_image)

#         # Display the processed image
#         st.subheader("Processed Image")
#         st.image(output_image, caption="Image with Background Removed", use_column_width=True)

# if __name__ == "__main__":
#     main()
import streamlit as st
from rembg import remove
from PIL import Image
import io

def remove_background(input_image):
    # Removing the background from the given image
    output_image = remove(input_image)
    return output_image

def main():
    st.markdown(
        """
        <h1 style='text-align: center; color: #eae6fa;'>Background Remover</h1>
        """,
        unsafe_allow_html=True)
    #Linkedin profile
    st.markdown(
        """
        <p style='text-align: center;'>Connect with me on <a href='https://www.linkedin.com/in/olti-gashi-a67098217/' style='color: #0077b5;'>LinkedIn</a></p>
        """,
        unsafe_allow_html=True
    )
    uploaded_file = st.file_uploader("Upload an image and remove the background", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        # Display uploaded image
        input_image = Image.open(uploaded_file)
        st.image(input_image, caption="Uploaded Image", use_column_width=True)

        # Process the image and remove background
        output_image = remove_background(input_image)

        # Display the processed image
        st.subheader("Processed Image")
        st.image(output_image, caption="Image with Background Removed", use_column_width=True)

        # Add a download button for the processed image
        output_stream = io.BytesIO()
        output_image.save(output_stream, format="PNG")  # You can change the format as needed
        output_stream.seek(0)
        st.download_button(
            label="Download Processed Image",
            data=output_stream,
            file_name="processed_image.png",  # Change the file name and extension as needed
            mime="image/png"
        )

if __name__ == "__main__":
    main()
