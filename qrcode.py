#!/usr/bin/env python
# coding: utf-8

# In[3]:


import qrcode

# Replace this URL with the link you want to convert to a QR code
link = "https://forms.office.com/r/ZdCd0fbpre"

# Create a QR code instance
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Add the link to the QR code
qr.add_data(link)
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill_color="black", back_color="white")

# Save the QR code as an image file
img.save("qr_code.png")

print("QR code generated and saved as qr_code.png")


# In[2]:


pip install qrcode[pil]


# In[ ]:




