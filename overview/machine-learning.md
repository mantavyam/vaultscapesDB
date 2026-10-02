---
icon: head-side-gear
---

# Machine Learning

An AI engineer solves a business problem with data, AI, and engineering, and puts the result in a product, so the model is one step on that path.

<a href="#collections-to-browse" class="button secondary">Jump to collections</a>

{% hint style="info" %}
**How projects were picked.** The code lives in the repo (or on the page), not just a link to somewhere else. The link works. The project teaches something real: data preparation, model building, evaluation, and ideally a small app.
{% endhint %}

{% hint style="warning" %}
**Read the badge on each card.** "No license" means students can read the repo for reference but should write their own code instead of copying it. "Archived" means the repo still works but is no longer updated.
**Last verified:** 2 October 2026. 
{% endhint %}

## Projects by level


{% tabs %}

{% tab title="Beginner" %}

<table data-view="cards"><thead><tr><th></th><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody>
<tr><td><strong>Heart disease prediction</strong></td><td>Tabular classification with a KNN model on patient data</td><td><em>Tabular · MIT</em></td><td><a href="https://github.com/kb22/Heart-Disease-Prediction">https://github.com/kb22/Heart-Disease-Prediction</a></td></tr>
<tr><td><strong>Handwritten digit recognition (MNIST)</strong></td><td>First CNN, train and save a model, run inference</td><td><em>Vision · MIT</em></td><td><a href="https://github.com/aakashjhawar/handwritten-digit-recognition">https://github.com/aakashjhawar/handwritten-digit-recognition</a></td></tr>
<tr><td><strong>Fake news detection</strong></td><td>TF-IDF features and a linear classifier in scikit-learn</td><td><em>Text · Free tutorial page</em></td><td><a href="https://data-flair.training/blogs/advanced-python-project-detecting-fake-news/">https://data-flair.training/blogs/advanced-python-project-detecting-fake-news/</a></td></tr>
<tr><td><strong>Walmart sales forecasting</strong></td><td>Regression on retail data, EDA, feature engineering</td><td><em>Forecasting · MIT</em></td><td><a href="https://github.com/gagandeepsinghkhanuja/Walmart-Sales-Forecasting">https://github.com/gagandeepsinghkhanuja/Walmart-Sales-Forecasting</a></td></tr>
<tr><td><strong>Human activity recognition</strong></td><td>Classifying smartphone sensor data (UCI HAR dataset)</td><td><em>Sensors · No license</em></td><td><a href="https://github.com/sushantdhumak/Human-Activity-Recognition-with-Smartphones">https://github.com/sushantdhumak/Human-Activity-Recognition-with-Smartphones</a></td></tr>
<tr><td><strong>Cats vs dogs image classifier</strong></td><td>CNN training on 18,000 images, reading training curves</td><td><em>Vision · No license</em></td><td><a href="https://github.com/anubhavparas/image-classification-using-cnn">https://github.com/anubhavparas/image-classification-using-cnn</a></td></tr>
<tr><td><strong>Mushroom classification</strong></td><td>A first neural network with TensorFlow/Keras on tabular data</td><td><em>Tabular · No license</em></td><td><a href="https://github.com/fiquinho/neural-network-projects">https://github.com/fiquinho/neural-network-projects</a></td></tr>
<tr><td><strong>Student performance prediction</strong></td><td>Classification and feature importance on a student dataset</td><td><em>Tabular · No license</em></td><td><a href="https://github.com/FaizanZaheerGit/StudentPerformancePrediction-ML">https://github.com/FaizanZaheerGit/StudentPerformancePrediction-ML</a></td></tr>
<tr><td><strong>Face detection with OpenCV</strong></td><td>Classical computer vision (Haar and LBP classifiers)</td><td><em>Vision · No license · Archived</em></td><td><a href="https://github.com/parulnith/Face-Detection-in-Python-using-OpenCV">https://github.com/parulnith/Face-Detection-in-Python-using-OpenCV</a></td></tr>
<tr><td><strong>Simple chatbot with NLTK</strong></td><td>Tokenizing, text similarity, rule-based responses</td><td><em>Text · No license · Archived</em></td><td><a href="https://github.com/parulnith/Building-a-Simple-Chatbot-in-Python-using-NLTK">https://github.com/parulnith/Building-a-Simple-Chatbot-in-Python-using-NLTK</a></td></tr>
<tr><td><strong>Student grade prediction</strong></td><td>Comparing several regressors and classifiers on 396 students; spotting data leakage</td><td><em>Tabular · MIT</em></td><td><a href="https://github.com/AbhishekMali21/STUDENT-GRADE-ANALYSIS-PREDICTION">https://github.com/AbhishekMali21/STUDENT-GRADE-ANALYSIS-PREDICTION</a></td></tr>
<tr><td><strong>Student dropout and success prediction</strong></td><td>Six classifiers compared on a 4,424-row UCI dataset</td><td><em>Tabular · No license</em></td><td><a href="https://github.com/hamzaezzine/Predict-students-dropout-and-academic-success-using-machine-learning-algorithms">https://github.com/hamzaezzine/Predict-students-dropout-and-academic-success-using-machine-learning-algorithms</a></td></tr>
<tr><td><strong>House price predictor (Flask)</strong></td><td>The smallest possible deployment: train, pickle, serve with Flask</td><td><em>App · No license</em></td><td><a href="https://github.com/Hritik21/House-Price-Predictor">https://github.com/Hritik21/House-Price-Predictor</a></td></tr>
<tr><td><strong>Titanic survival (Streamlit app)</strong></td><td>A notebook pipeline plus a Streamlit front end</td><td><em>App · No license</em></td><td><a href="https://github.com/yasirali646/titanic-death-predictor">https://github.com/yasirali646/titanic-death-predictor</a></td></tr>
<tr><td><strong>Color mood API</strong></td><td>A KNN model served behind a small FastAPI service</td><td><em>App · MIT</em></td><td><a href="https://github.com/gggff123/color-api">https://github.com/gggff123/color-api</a></td></tr>
</tbody></table>

{% hint style="info" %}
The two `parulnith` repos are archived (read-only). The code still works for learning, but nobody is updating it.
{% endhint %}

{% hint style="info" %}
**Student grade prediction.** The README itself notes that the final grade (G3) is strongly tied to earlier grades (G1, G2). Ask students to rerun the models without G1 and G2 and compare; it is a good lesson in leakage.
{% endhint %}

{% hint style="info" %}
For wine quality or breast cancer classification, the UCI datasets are clean and CC BY 4.0 licensed, so students can write the code from scratch:

* https://archive.ics.uci.edu/dataset/186/wine+quality
* https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic
{% endhint %}

{% endtab %}

{% tab title="Intermediate" %}

<table data-view="cards"><thead><tr><th></th><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody>
<tr><td><strong>Twitter sentiment analysis</strong></td><td>Comparing Naive Bayes, SVM, LSTM and CNN on the same text task</td><td><em>Text · MIT · Archived</em></td><td><a href="https://github.com/abdulfatir/twitter-sentiment-analysis">https://github.com/abdulfatir/twitter-sentiment-analysis</a></td></tr>
<tr><td><strong>CNN from scratch in NumPy</strong></td><td>How convolution, pooling and softmax actually work, with no framework</td><td><em>Vision · MIT</em></td><td><a href="https://github.com/vzhou842/cnn-from-scratch">https://github.com/vzhou842/cnn-from-scratch</a></td></tr>
<tr><td><strong>Driver drowsiness detection</strong></td><td>Live webcam inference with a CNN on eye state, plus an alarm</td><td><em>Vision · No license</em></td><td><a href="https://github.com/abhishek351/Driver-drowsiness-detection-CNN-Keras-OpenCV">https://github.com/abhishek351/Driver-drowsiness-detection-CNN-Keras-OpenCV</a></td></tr>
<tr><td><strong>Music genre classification</strong></td><td>Audio spectrograms with CNN/RNN on the GTZAN dataset</td><td><em>Audio · MIT</em></td><td><a href="https://github.com/jsalbert/Music-Genre-Classification-with-Deep-Learning">https://github.com/jsalbert/Music-Genre-Classification-with-Deep-Learning</a></td></tr>
<tr><td><strong>Movie recommendation system (web app)</strong></td><td>TF-IDF and SVD recommender served in a Django app</td><td><em>Recommender · MIT</em></td><td><a href="https://github.com/inboxpraveen/Movie-Recommendation-System">https://github.com/inboxpraveen/Movie-Recommendation-System</a></td></tr>
<tr><td><strong>Matrix factorization recommender</strong></td><td>Collaborative filtering on MovieLens</td><td><em>Recommender · No license</em></td><td><a href="https://github.com/SurhanZahid/Recommendation-System-Using-Matrix-Factorization">https://github.com/SurhanZahid/Recommendation-System-Using-Matrix-Factorization</a></td></tr>
<tr><td><strong>Customer lifetime value (with Streamlit app)</strong></td><td>RFM features, BG-NBD and Gamma-Gamma models, simple deployment</td><td><em>Tabular · No license</em></td><td><a href="https://github.com/mukulsinghal001/customer-lifetime-prediction-using-python">https://github.com/mukulsinghal001/customer-lifetime-prediction-using-python</a></td></tr>
<tr><td><strong>Deep learning chatbot (Flask)</strong></td><td>Intent classification and a small web interface</td><td><em>Text · MIT</em></td><td><a href="https://github.com/Karan-Malik/Chatbot">https://github.com/Karan-Malik/Chatbot</a></td></tr>
<tr><td><strong>English to French translation</strong></td><td>Encoder-decoder (Seq2Seq) model in Keras</td><td><em>Text · No license</em></td><td><a href="https://github.com/lukysummer/Machine-Translation-Seq2Seq-Keras">https://github.com/lukysummer/Machine-Translation-Seq2Seq-Keras</a></td></tr>
<tr><td><strong>Zillow house price error prediction</strong></td><td>Gradient boosting (LightGBM, CatBoost) and model stacking</td><td><em>Tabular · No license</em></td><td><a href="https://github.com/junjiedong/Zillow-Kaggle">https://github.com/junjiedong/Zillow-Kaggle</a></td></tr>
<tr><td><strong>Wind turbine predictive maintenance</strong></td><td>Cost-aware classification on sensor data</td><td><em>Sensors · No license</em></td><td><a href="https://github.com/rochitasundar/Predictive-maintenance-cost-minimization-using-ML-ReneWind">https://github.com/rochitasundar/Predictive-maintenance-cost-minimization-using-ML-ReneWind</a></td></tr>
<tr><td><strong>Software bug prediction</strong></td><td>Dimensionality reduction (PCA) and class balancing on code metrics</td><td><em>Tabular · No license</em></td><td><a href="https://github.com/YousefGh/software_bug_prediction">https://github.com/YousefGh/software_bug_prediction</a></td></tr>
<tr><td><strong>Stock price forecasting with GRU</strong></td><td>Time series deep learning on 12 years of price data</td><td><em>Forecasting · No license</em></td><td><a href="https://github.com/soham2707/Stock-Market-Analysis-And-Forecasting-Using-Deep-Learning">https://github.com/soham2707/Stock-Market-Analysis-And-Forecasting-Using-Deep-Learning</a></td></tr>
<tr><td><strong>Plant leaf disease prediction</strong></td><td>The same task in PyTorch, TensorFlow, Keras and fastai, with a desktop GUI</td><td><em>Vision · MIT</em></td><td><a href="https://github.com/PuneethReddyHC/leaf-diseases-predition">https://github.com/PuneethReddyHC/leaf-diseases-predition</a></td></tr>
<tr><td><strong>Sign language recognition</strong></td><td>Hand segmentation in OpenCV and a CNN classifier</td><td><em>Vision · Free tutorial page</em></td><td><a href="https://data-flair.training/blogs/sign-language-recognition-python-ml-opencv/">https://data-flair.training/blogs/sign-language-recognition-python-ml-opencv/</a></td></tr>
<tr><td><strong>Face recognition attendance system</strong></td><td>Building an app on a face recognition library (webcam, face encodings, matching). The repo has example scripts, including a web service.</td><td><em>Vision · MIT</em></td><td><a href="https://github.com/ageitgey/face_recognition">https://github.com/ageitgey/face_recognition</a></td></tr>
<tr><td><strong>Indian sign language recognition</strong></td><td>OpenCV hand detection with Keras and PyTorch models on Sign Language MNIST</td><td><em>Vision · Apache-2.0</em></td><td><a href="https://github.com/Arshad221b/Sign-Language-Recognition">https://github.com/Arshad221b/Sign-Language-Recognition</a></td></tr>
<tr><td><strong>Driver drowsiness detection (Streamlit)</strong></td><td>Blink detection from facial landmarks, with a Streamlit web app</td><td><em>Vision · MIT</em></td><td><a href="https://github.com/Gagandeep-2003/driver-drowsiness-detection-system">https://github.com/Gagandeep-2003/driver-drowsiness-detection-system</a></td></tr>
<tr><td><strong>Fast text classification with fastText</strong></td><td>Training word vectors and a supervised text classifier, then comparing it with a TF-IDF baseline</td><td><em>Text · MIT · Archived</em></td><td><a href="https://github.com/facebookresearch/fastText">https://github.com/facebookresearch/fastText</a></td></tr>
</tbody></table>

{% hint style="info" %}
The chatbot README links to a Heroku demo. Heroku ended free hosting in 2022, so expect that demo not to load and have students run the app locally.
{% endhint %}

{% hint style="info" %}
The DataFlair sign language tutorial pins old versions (TensorFlow 2.0, Keras 2.3.1). Updating it to current versions is a good exercise in itself.
{% endhint %}

{% hint style="info" %}
Present the stock forecasting project as a time series exercise, not as a trading tool.
{% endhint %}

{% hint style="info" %}
The fastText repo was archived in March 2024. It still works, but it is no longer updated.
{% endhint %}

{% hint style="info" %}
For the face recognition project, students should use their own or consenting classmates' photos only.
{% endhint %}

{% endtab %}

{% tab title="Advanced" %}

<table data-view="cards"><thead><tr><th></th><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody>
<tr><td><strong>Fake news classification with BERT and RoBERTa (full app)</strong></td><td>Fine-tuning transformers, Flask backend, Streamlit frontend, Docker</td><td><em>Text · MIT</em></td><td><a href="https://github.com/hritik5102/Fake-news-classification-model">https://github.com/hritik5102/Fake-news-classification-model</a></td></tr>
<tr><td><strong>Land cover segmentation from satellite images</strong></td><td>Semantic segmentation in PyTorch, config-driven training and inference</td><td><em>Vision · MIT</em></td><td><a href="https://github.com/souvikmajumder26/Land-Cover-Semantic-Segmentation-PyTorch">https://github.com/souvikmajumder26/Land-Cover-Semantic-Segmentation-PyTorch</a></td></tr>
<tr><td><strong>One-shot face stylization (JoJoGAN)</strong></td><td>GAN inversion and fine-tuning StyleGAN; runs in Colab</td><td><em>Generative · MIT</em></td><td><a href="https://github.com/mchong6/JoJoGAN">https://github.com/mchong6/JoJoGAN</a></td></tr>
<tr><td><strong>Image generation with a GAN</strong></td><td>Building a generator and discriminator on CIFAR-10</td><td><em>Generative · MIT</em></td><td><a href="https://github.com/abhi227070/Image-Generation-Using-GAN-Gen-AI-Project-">https://github.com/abhi227070/Image-Generation-Using-GAN-Gen-AI-Project-</a></td></tr>
<tr><td><strong>Multi-modal house price estimation</strong></td><td>Combining image and text features in one model</td><td><em>Multimodal · No license</em></td><td><a href="https://github.com/Mehrab-Kalantari/Multi-Modal-House-Price-Estimation">https://github.com/Mehrab-Kalantari/Multi-Modal-House-Price-Estimation</a></td></tr>
<tr><td><strong>Orca (killer whale) call classifier</strong></td><td>Mel-spectrograms and audio deep learning on real hydrophone data</td><td><em>Audio · No license</em></td><td><a href="https://github.com/rohankrgupta/Orca-call-Classifier-Machine-learning">https://github.com/rohankrgupta/Orca-call-Classifier-Machine-learning</a></td></tr>
<tr><td><strong>Music generation with C-RNN-GAN</strong></td><td>Sequence modeling and GANs on MIDI data</td><td><em>Generative · MIT</em></td><td><a href="https://github.com/seyedsaleh/music-generator">https://github.com/seyedsaleh/music-generator</a></td></tr>
<tr><td><strong>Drug discovery with ChEMBL data</strong></td><td>Molecular descriptors and regression for bioactivity</td><td><em>Science · No license</em></td><td><a href="https://github.com/shashwat0105/Bioinformatics-Drug-Discovery">https://github.com/shashwat0105/Bioinformatics-Drug-Discovery</a></td></tr>
<tr><td><strong>Bosch production line failures</strong></td><td>Very wide, sparse tabular data with XGBoost</td><td><em>Tabular · No license</em></td><td><a href="https://github.com/aakashveera/bosch-production-line-performance">https://github.com/aakashveera/bosch-production-line-performance</a></td></tr>
<tr><td><strong>Network intrusion prevention</strong></td><td>Anomaly detection on live traffic, FastAPI service, Linux iptables</td><td><em>Security · MIT</em></td><td><a href="https://github.com/zimingttkx/Network-Security-Based-On-ML">https://github.com/zimingttkx/Network-Security-Based-On-ML</a></td></tr>
<tr><td><strong>Self-driving car projects</strong></td><td>Lane detection, traffic sign classification, behavioral cloning</td><td><em>Vision · No license</em></td><td><a href="https://github.com/vatsl/AutonomousDriving">https://github.com/vatsl/AutonomousDriving</a></td></tr>
<tr><td><strong>LLM fine-tuning with QLoRA</strong></td><td>Fine-tuning a 4-bit Llama 2 model on a Q&amp;A dataset</td><td><em>LLM · No license</em></td><td><a href="https://github.com/Cody-Lange/MentalHealthAssistant">https://github.com/Cody-Lange/MentalHealthAssistant</a></td></tr>
<tr><td><strong>Full-song generation with diffusion (DiffRhythm)</strong></td><td>Running and extending a modern latent diffusion model</td><td><em>Generative · Apache-2.0</em></td><td><a href="https://github.com/ASLP-lab/DiffRhythm">https://github.com/ASLP-lab/DiffRhythm</a></td></tr>
<tr><td><strong>Build a GPT from scratch</strong></td><td>Backpropagation, a character-level language model, then a small GPT and a tokenizer, following 8 video lectures</td><td><em>LLM · MIT</em></td><td><a href="https://github.com/karpathy/nn-zero-to-hero">https://github.com/karpathy/nn-zero-to-hero</a></td></tr>
<tr><td><strong>Train a small GPT (nanoGPT)</strong></td><td>Training a GPT on your own text, starting with a character-level Shakespeare model; a good follow-up to the lectures</td><td><em>LLM · MIT</em></td><td><a href="https://github.com/karpathy/nanoGPT">https://github.com/karpathy/nanoGPT</a></td></tr>
<tr><td><strong>Train a full small chatbot (nanochat)</strong></td><td>The whole pipeline: tokenizer, pretraining, fine-tuning, evaluation and a chat web UI</td><td><em>LLM · MIT</em></td><td><a href="https://github.com/karpathy/nanochat">https://github.com/karpathy/nanochat</a></td></tr>
<tr><td><strong>Video object segmentation and tracking (SAM 2)</strong></td><td>Using a foundation model to segment and track objects in images and video, then building an app around it</td><td><em>Vision · Apache-2.0, BSD-3-Clause</em></td><td><a href="https://github.com/facebookresearch/sam2">https://github.com/facebookresearch/sam2</a></td></tr>
<tr><td><strong>Build with Llama (RAG and fine-tuning)</strong></td><td>Official recipes for inference, fine-tuning and RAG with Llama models</td><td><em>LLM · MIT</em></td><td><a href="https://github.com/meta-llama/llama-cookbook">https://github.com/meta-llama/llama-cookbook</a></td></tr>
<tr><td><strong>Flower classification (102 classes)</strong></td><td>Comparing EfficientNet, InceptionV3 and ResNet, with saliency maps and Grad-CAM</td><td><em>Vision · MIT</em></td><td><a href="https://github.com/firaja/flowers-classification">https://github.com/firaja/flowers-classification</a></td></tr>
<tr><td><strong>Generative AI foundations in PyTorch</strong></td><td>Short scripts on entropy, KL divergence, MCMC, VAEs, transformers, LoRA and GANs</td><td><em>Generative · MIT</em></td><td><a href="https://github.com/SimoneFaraulo/GenerativeAI-Foundations">https://github.com/SimoneFaraulo/GenerativeAI-Foundations</a></td></tr>
<tr><td><strong>Traffic sign robot (hardware)</strong></td><td>Sign recognition on a camera feed that steers an Arduino robot through ROS</td><td><em>Robotics · No license</em></td><td><a href="https://github.com/djr111/OpenCV_Traffic_Sign_Detection_Arduino_Robot">https://github.com/djr111/OpenCV_Traffic_Sign_Detection_Arduino_Robot</a></td></tr>
</tbody></table>

{% hint style="warning" %}
**GPU requirements.** JoJoGAN, the QLoRA fine-tuning project and DiffRhythm all need a GPU. DiffRhythm needs at least 8 GB of VRAM. Google Colab is enough for JoJoGAN.
{% endhint %}

{% hint style="warning" %}
**Mental health assistant.** The QLoRA project is trained on mental health Q&A. If you assign it, ask students to switch to a different domain or add clear safety disclaimers.
{% endhint %}

{% hint style="warning" %}
**Network intrusion project.** It changes firewall rules, so run it only inside a VM.
{% endhint %}

{% hint style="warning" %}
**Traffic sign robot.** It needs an Arduino robot, a USB camera and Ubuntu, and the repo has no license. It fits only teams with access to a robotics lab.
{% endhint %}

{% hint style="warning" %}
**SAM 2.** It needs Python 3.10+, PyTorch 2.5.1+ and a GPU. The repo has Colab notebooks for image and video prediction, which are the easiest way to start.
{% endhint %}

{% hint style="info" %}
**Llama Cookbook.** Each Llama model has its own license and acceptable use policy, linked from the repo. Students need to accept these before downloading the weights.
{% endhint %}

{% hint style="warning" %}
**nanoGPT and nanochat.** The nanoGPT README now marks it as "very old and deprecated" and points to nanochat. It still works and has a section on training on a MacBook or other cheap computer, so it is the easier student project. nanochat's full run targets an 8xH100 GPU node (about $48 of cloud time per the README). It also runs on a single GPU (about 8 times slower) or on CPU with a much smaller model, so assign it only to students with GPU access.
{% endhint %}

{% endtab %}

{% endtabs %}


## Collections to browse

Repos and competitions with many projects in one place, for students who want to go further.


<table data-view="cards"><thead><tr><th></th><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody>
<tr><td><strong>shsarv/Machine-Learning-Projects</strong></td><td>26 projects with code in the repo, several with Flask or desktop GUIs.</td><td><em>MIT</em></td><td><a href="https://github.com/shsarv/Machine-Learning-Projects">https://github.com/shsarv/Machine-Learning-Projects</a></td></tr>
<tr><td><strong>devAmoghS/Machine-Learning-with-Python</strong></td><td>19 small scikit-learn and Keras projects (spam filter, churn, clustering).</td><td><em>MIT</em></td><td><a href="https://github.com/devAmoghS/Machine-Learning-with-Python">https://github.com/devAmoghS/Machine-Learning-with-Python</a></td></tr>
<tr><td><strong>tanveer-kader/ml-projects-py</strong></td><td>25 beginner notebooks (rock vs mine, diabetes, house prices, fake news, face masks).</td><td><em>MIT</em></td><td><a href="https://github.com/tanveer-kader/ml-projects-py">https://github.com/tanveer-kader/ml-projects-py</a></td></tr>
<tr><td><strong>Abhinav-26/Machine-Learning-Minor-Projects</strong></td><td>Beginner and intermediate projects, from regression to dog breed classification and Reddit flair detection.</td><td><em>MIT</em></td><td><a href="https://github.com/Abhinav-26/Machine-Learning-Minor-Projects">https://github.com/Abhinav-26/Machine-Learning-Minor-Projects</a></td></tr>
<tr><td><strong>anubhavshrimal/Machine-Learning</strong></td><td>Algorithms plus deep learning, image captioning, GANs and RL, in several frameworks. Last updated in 2020, so expect old library versions.</td><td><em>MIT</em></td><td><a href="https://github.com/anubhavshrimal/Machine-Learning">https://github.com/anubhavshrimal/Machine-Learning</a></td></tr>
<tr><td><strong>milaan9/93_Python_Data_Analytics_Projects</strong></td><td>Notebooks for data analytics and ML (resume screening, X-ray CNN, LSTM translation).</td><td><em>MIT</em></td><td><a href="https://github.com/milaan9/93_Python_Data_Analytics_Projects">https://github.com/milaan9/93_Python_Data_Analytics_Projects</a></td></tr>
<tr><td><strong>ZenithClown/ai-ml-project-template</strong></td><td>A starting folder layout for an ML project.</td><td><em>MIT</em></td><td><a href="https://github.com/ZenithClown/ai-ml-project-template">https://github.com/ZenithClown/ai-ml-project-template</a></td></tr>
<tr><td><strong>faridrashidi/kaggle-solutions</strong></td><td>Winning Kaggle solutions and write-ups, grouped by problem type. Good for advanced students.</td><td><em>MIT</em></td><td><a href="https://github.com/faridrashidi/kaggle-solutions">https://github.com/faridrashidi/kaggle-solutions</a></td></tr>
<tr><td><strong>ageron/handson-ml3</strong></td><td>Notebooks for every chapter of the book <em>Hands-On Machine Learning</em> (3rd edition), from classification to deep learning and RL. Opens in Colab.</td><td><em>Apache-2.0</em></td><td><a href="https://github.com/ageron/handson-ml3">https://github.com/ageron/handson-ml3</a></td></tr>
<tr><td><strong>eriklindernoren/ML-From-Scratch</strong></td><td>NumPy implementations of about 30 algorithms (regression, trees, SVM, k-means, GANs, DQN). Good for "implement it yourself" assignments.</td><td><em>MIT</em></td><td><a href="https://github.com/eriklindernoren/ML-From-Scratch">https://github.com/eriklindernoren/ML-From-Scratch</a></td></tr>
<tr><td><strong>khuyentran1401/data-science-template</strong></td><td>A project template, not a project: folder structure, Hydra config, pre-commit and docs. Useful to make every student project follow the same layout.</td><td><em>MIT</em></td><td><a href="https://github.com/khuyentran1401/data-science-template">https://github.com/khuyentran1401/data-science-template</a></td></tr>
<tr><td><strong>anidec25/ML-Projects</strong></td><td>Notebooks grouped by algorithm (regression, trees, ensembles, clustering, PCA, time series).</td><td><em>No license</em></td><td><a href="https://github.com/anidec25/ML-Projects">https://github.com/anidec25/ML-Projects</a></td></tr>
<tr><td><strong>lukas/ml-class</strong></td><td>Teaching projects "designed for engineers": Fashion MNIST, autoencoders, sentiment analysis, RNNs, text generation, transfer learning. Each has a short video.</td><td><em>GPL-2.0</em></td><td><a href="https://github.com/lukas/ml-class">https://github.com/lukas/ml-class</a></td></tr>
<tr><td><strong>rhiever/Data-Analysis-and-Machine-Learning-Projects</strong></td><td>Teaching notebooks tied to blog posts (TPOT demo, route optimization, data visualization). Older, but code and data are in the repo.</td><td><em>CC BY 4.0 and MIT (see README)</em></td><td><a href="https://github.com/rhiever/Data-Analysis-and-Machine-Learning-Projects">https://github.com/rhiever/Data-Analysis-and-Machine-Learning-Projects</a></td></tr>
<tr><td><strong>NirantK/awesome-project-ideas</strong></td><td>Project ideas with datasets and links to prior work. Ideas only, no code.</td><td><em>MIT</em></td><td><a href="https://github.com/NirantK/awesome-project-ideas">https://github.com/NirantK/awesome-project-ideas</a></td></tr>
<tr><td><strong>Kaggle: Store Sales forecasting</strong></td><td>A beginner-friendly time series competition with many public notebooks</td><td><em>Kaggle competition</em></td><td><a href="https://www.kaggle.com/competitions/store-sales-time-series-forecasting">https://www.kaggle.com/competitions/store-sales-time-series-forecasting</a></td></tr>
<tr><td><strong>Kaggle: H&amp;M fashion recommendations</strong></td><td>A large real-world recommendation dataset</td><td><em>Kaggle competition</em></td><td><a href="https://www.kaggle.com/competitions/h-and-m-personalized-fashion-recommendations">https://www.kaggle.com/competitions/h-and-m-personalized-fashion-recommendations</a></td></tr>
</tbody></table>