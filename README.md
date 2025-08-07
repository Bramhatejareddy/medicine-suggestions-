# Personalized Medicine Suggestions and Reminder Alerts for Elderly Care

## Overview

This project presents an AI-powered application designed to assist elderly individuals in managing their medication routines through personalized medicine recommendations and intelligent reminder alerts. Built using Python, Streamlit, and SQLite3, the system combines modern pharmaceuticals with traditional remedies, ensuring timely medication adherence and enhanced healthcare outcomes.

## Problem Statement

Elderly users often face challenges managing multiple prescriptions, understanding dosage schedules, and remembering timely intake. Traditional systems generally lack personalization, often ignoring user preferences, medical history, or traditional health practices. This system addresses these gaps by offering tailored drug suggestions and customizable alerts that ensure the right medicine is taken at the right time.

## Key Features

- **Personalized Medicine Recommendations**  
  Utilizes TF-IDF and cosine similarity to suggest medicines based on a user’s medical history, current conditions, and preferences.

- **Traditional Remedies Integration**  
  Supports alternative medicine preferences by recommending safe and relevant herbal or homeopathic treatments.

- **Smart Reminder Alert System**  
  Offers customizable, audible, and visual reminders to help users take medicines on time.

- **Secure User Profile Management**  
  Allows users to maintain and update health records, preferences, allergies, and dosage schedules.

- **Streamlined Data Management**  
  Uses SQLite3 for efficient, local data handling and fast storage/retrieval.

## Technology Stack

- **Frontend:** Streamlit (Python-based UI framework)
- **Backend:** Python
- **Database:** SQLite3
- **ML Techniques:** TF-IDF, Cosine Similarity
- **Others:** Data preprocessing, feature extraction, basic NLP techniques

## How It Works

1. **User Registration & Profile Setup:**  
   Users input personal details, medical history, and preferences.

2. **Data Preprocessing:**  
   Cleans and formats both user health data and drug database.

3. **Recommendation Engine:**  
   Matches health profiles with relevant medications and traditional remedies using vector-based similarity.

4. **Alert Module:**  
   Sends visual and audio alerts based on customized medication schedules.

5. **User Interface:**  
   A simple and accessible Streamlit-based interface designed for elderly usability.

## Results

The system has shown high accuracy and usability in real-time tests. Users receive timely suggestions and reminders that reduce missed doses and improve health outcomes. The inclusion of traditional remedies has been positively received by users preferring holistic healthcare approaches.

## Future Enhancements

- Drug interaction warnings for increased safety
- Integration with wearable devices for real-time health tracking
- Caregiver and family member collaboration features
- Multilingual support for wider accessibility
- Gamified adherence tracking to encourage consistent use

## Deployment

This application is deployed using Streamlit Cloud. It is accessible via a web browser and does not require any installation from the user’s side.

> 🔗 **Live Demo**: [https://your-username-your-app.streamlit.app](#)  
> *(Replace with actual link after deployment)*

## Author

G.Bramha teja reddy 
Department of Computer Science and Engineering  
K.S.R.M. College of Engineering, Kadapa

## License

This project is licensed for academic and research use. Contact the author for commercial or collaborative usage.

---

