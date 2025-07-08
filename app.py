import streamlit as st
import tensorflow as tf
import numpy as np
from tensorflow.keras.models import load_model

# === Load model ===
model = load_model(r'C:\Users\Syed\Desktop\fruit and vegetables img classifications\image_classifications.keras')

# === Category list ===
data_cat = [
    'apple', 'banana', 'beetroot', 'bell pepper', 'cabbage', 'capsicum', 'carrot', 'cauliflower',
    'chilli pepper', 'corn', 'cucumber', 'eggplant', 'garlic', 'ginger', 'grapes', 'jalepeno',
    'kiwi', 'lemon', 'lettuce', 'mango', 'onion', 'orange', 'paprika', 'pear', 'peas',
    'sweetcorn', 'sweetpotato', 'tomato', 'turnip', 'watermelon'
]

# === Image size ===
img_height, img_width = 180, 180

# === Page config ===
st.set_page_config(page_title="ফল ও সবজি শনাক্তকরণ 🍓🥦", layout="centered")

# === Custom CSS ===
st.markdown("""
    <style>
        .main-title {
            background: linear-gradient(to right, #00c6ff, #0072ff);
            color: white;
            padding: 1rem;
            border-radius: 0.5rem;
            text-align: center;
            font-size: 2rem;
            margin-bottom: 1.5rem;
        }
        .footer {
            margin-top: 2rem;
            text-align: center;
            color: #888;
            font-size: 0.9rem;
        }
    </style>
""", unsafe_allow_html=True)

# === Gradient title ===
st.markdown('<div class="main-title">🥗 ফল ও সবজি শনাক্তকরণ 🥝</div>', unsafe_allow_html=True)

# === Bangla Nutrition Info ===
nutrition_bn = {
    "apple": {"name": "আপেল", "calories": "৫২ ক্যালোরি প্রতি ১০০ গ্রাম", "benefits": "আপেল হজমে সাহায্য করে এবং হৃদয় সুস্থ রাখে।"},
    "banana": {"name": "কলা", "calories": "৮৯ ক্যালোরি প্রতি ১০০ গ্রাম", "benefits": "কলা শক্তি যোগায় এবং হজমে সাহায্য করে।"},
    "beetroot": {"name": "বীটরুট", "calories": "৪৩ ক্যালোরি", "benefits": "বীটরুট রক্তচাপ কমায় এবং রক্ত তৈরি করে।"},
    "bell pepper": {"name": "বেল পিপার", "calories": "২০ ক্যালোরি", "benefits": "বেল পিপার অ্যান্টিঅক্সিডেন্ট সমৃদ্ধ।"},
    "cabbage": {"name": "বাঁধাকপি", "calories": "২৫ ক্যালোরি", "benefits": "বাঁধাকপি ক্যান্সার প্রতিরোধে সাহায্য করে।"},
    "capsicum": {"name": "ক্যাপসিকাম", "calories": "২০ ক্যালোরি", "benefits": "ক্যাপসিকাম রোগ প্রতিরোধে সাহায্য করে।"},
    "carrot": {"name": "গাজর", "calories": "৪১ ক্যালোরি", "benefits": "গাজর চোখের দৃষ্টিশক্তি ভালো রাখে।"},
    "cauliflower": {"name": "ফুলকপি", "calories": "২৫ ক্যালোরি", "benefits": "ফুলকপি হজমে সাহায্য করে এবং ফাইবার সমৃদ্ধ।"},
    "chilli pepper": {"name": "লাল মরিচ", "calories": "৪০ ক্যালোরি", "benefits": "লাল মরিচ বিপাকক্রিয়া বাড়ায়।"},
    "corn": {"name": "ভুট্টা", "calories": "৯৬ ক্যালোরি", "benefits": "ভুট্টা শক্তি যোগায় এবং আঁশে ভরপুর।"},
    "cucumber": {"name": "শসা", "calories": "১৬ ক্যালোরি", "benefits": "শসা শরীর ঠান্ডা রাখে এবং জলীয় উপাদানে সমৃদ্ধ।"},
    "eggplant": {"name": "বেগুন", "calories": "২৫ ক্যালোরি", "benefits": "বেগুন হার্টের স্বাস্থ্য রক্ষা করে।"},
    "garlic": {"name": "রসুন", "calories": "১৪৯ ক্যালোরি", "benefits": "রসুন রক্তচাপ কমায় এবং জীবাণু প্রতিরোধ করে।"},
    "ginger": {"name": "আদা", "calories": "৮০ ক্যালোরি", "benefits": "আদা হজমে সহায়ক এবং প্রদাহ কমায়।"},
    "grapes": {"name": "আঙুর", "calories": "৬৭ ক্যালোরি", "benefits": "আঙুর অ্যান্টিঅক্সিডেন্ট সমৃদ্ধ।"},
    "jalepeno": {"name": "জালাপেনো", "calories": "২৯ ক্যালোরি", "benefits": "জালাপেনো বিপাকক্রিয়া বাড়ায় এবং রোগ প্রতিরোধে সহায়ক।"},
    "kiwi": {"name": "কিউই", "calories": "৪১ ক্যালোরি", "benefits": "কিউই ভিটামিন C সমৃদ্ধ এবং ত্বকের জন্য উপকারী।"},
    "lemon": {"name": "লেবু", "calories": "২৯ ক্যালোরি", "benefits": "লেবু ভিটামিন C সমৃদ্ধ এবং রোগ প্রতিরোধে সহায়ক।"},
    "lettuce": {"name": "লেটুস", "calories": "১৫ ক্যালোরি", "benefits": "লেটুস ওজন কমাতে সহায়ক।"},
    "mango": {"name": "আম", "calories": "৬০ ক্যালোরি", "benefits": "আম ভিটামিন A এবং আঁশে ভরপুর।"},
    "onion": {"name": "পেঁয়াজ", "calories": "৪০ ক্যালোরি", "benefits": "পেঁয়াজ রক্তে চিনির মাত্রা নিয়ন্ত্রণে সহায়ক।"},
    "orange": {"name": "কমলা", "calories": "৪৭ ক্যালোরি", "benefits": "কমলা ভিটামিন C সমৃদ্ধ এবং রোগ প্রতিরোধে সহায়ক।"},
    "paprika": {"name": "পাপরিকা", "calories": "২৮২ ক্যালোরি (মসলা হিসেবে)", "benefits": "পাপরিকা প্রদাহ কমাতে সহায়ক।"},
    "pear": {"name": "নাশপাতি", "calories": "৫৭ ক্যালোরি", "benefits": "নাশপাতি হজমে সহায়ক এবং আঁশে ভরপুর।"},
    "peas": {"name": "মটরশুঁটি", "calories": "৮১ ক্যালোরি", "benefits": "মটরশুঁটি প্রোটিন সমৃদ্ধ এবং হাড়ের জন্য উপকারী।"},
    "pineapple": {"name": "আনারস", "calories": "৫০ ক্যালোরি", "benefits": "আনারস হজমে সহায়ক এবং রোগ প্রতিরোধে সহায়ক।"},
    "pomegranate": {"name": "ডালিম", "calories": "৮৩ ক্যালোরি", "benefits": "ডালিম রক্তচাপ নিয়ন্ত্রণে সহায়ক।"},
    "potato": {"name": "আলু", "calories": "৭৭ ক্যালোরি", "benefits": "আলু শক্তি যোগায়, কিন্তু বেশি না খাওয়াই ভালো।"},
    "raddish": {"name": "মূলা", "calories": "১৬ ক্যালোরি", "benefits": "মূলা হজমে সহায়ক এবং লিভারের জন্য উপকারী।"},
    "soy beans": {"name": "সয়াবিন", "calories": "৪৪৬ ক্যালোরি", "benefits": "সয়াবিন প্রোটিন এবং ক্যালসিয়াম সমৃদ্ধ।"},
    "spinach": {"name": "পালং শাক", "calories": "২৩ ক্যালোরি", "benefits": "পালং শাক আয়রন সমৃদ্ধ এবং রক্ত বাড়ায়।"},
    "sweetcorn": {"name": "মিষ্টি ভুট্টা", "calories": "৮৬ ক্যালোরি", "benefits": "মিষ্টি ভুট্টা শক্তি দেয় এবং আঁশে ভরপুর।"},
    "sweetpotato": {"name": "মিষ্টি আলু", "calories": "৮৬ ক্যালোরি", "benefits": "মিষ্টি আলু ভিটামিন A সমৃদ্ধ এবং হজমে সহায়ক।"},
    "turnip": {"name": "শালগম", "calories": "২৮ ক্যালোরি", "benefits": "শালগম হাড় মজবুত রাখতে সহায়ক।"}
}

# === Upload section ===

uploaded_file = st.file_uploader("একটি ফল বা সবজির ছবি আপলোড করুন", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    try:
        # === Load and preprocess image ===
        image = tf.keras.utils.load_img(uploaded_file, target_size=(img_height, img_width))
        img_array = tf.keras.utils.img_to_array(image)
        img_batch = tf.expand_dims(img_array, 0)

        # === Prediction ===
        prediction = model.predict(img_batch)
        confidence = tf.nn.softmax(prediction[0])
        predicted_class = data_cat[np.argmax(confidence)]

        # === Layout with columns ===
        col1, col2 = st.columns(2)

        # === Left: Image + Prediction ===
        with col1:
            st.image(uploaded_file, caption="🖼️ আপলোড করা ছবি", width=280)
            st.markdown("## 🧠 পূর্বাভাস ফলাফল:")
            if predicted_class in nutrition_bn:
                info = nutrition_bn[predicted_class]
                st.success(f"🔍 **সনাক্তকৃত নাম:** `{info['name']}`")
            else:
                st.success(f"🔍 **সনাক্তকৃত নাম:** `{predicted_class.title()}`")
            st.write(f"✅ **Accuracy:** `{np.max(confidence) * 100:.2f}%`")

        # === Right: Nutrition Info ===
        with col2:
            st.markdown("## 🥗 পুষ্টি তথ্য:")
            if predicted_class in nutrition_bn:
                st.write(f"**নাম:** {info['name']}")
                st.write(f"**ক্যালোরি:** {info['calories']}")
                st.write(f"**উপকারিতা:** {info['benefits']}")
            else:
                st.info("🔎 এই উপাদানের জন্য বাংলা তথ্য পাওয়া যায়নি।")

    except Exception as e:
        st.error(f"❌ সমস্যা হয়েছে: {e}")

# === Footer ===
st.markdown('<div class="footer">Created by Sami & Tamim</div>', unsafe_allow_html=True)
