# 📞 Event-Driven Customer Support & Fitness Routine Recommender

Welcome to the **Event-Driven Customer Support & Fitness Routine Recommender** project! This project is a web application that provides two main functionalities: a customer support system and a fitness routine recommender. Both features are designed to enhance user experience by automating processes and providing personalized services.

## 🚀 Features

1. **Customer Support System**:
   - Users can submit support tickets through a form.
   - Tickets are automatically classified and assigned to the appropriate support team based on the content.
   - Notifications are sent to the assigned team member via Discord.

2. **Fitness Routine Recommender**:
   - Users can input personal details to receive a personalized fitness routine.
   - The routine is sent to the user via Discord.
   - A weekly fitness routine is scheduled to be sent every Sunday.

## 🛠 Benefits

1. **Automated Customer Support**: Streamlines the support process by automatically classifying and assigning tickets, reducing response time and improving customer satisfaction.

2. **Personalized Fitness Recommendations**: Offers tailored fitness routines based on user input, enhancing user engagement and promoting healthier lifestyles.

3. **Seamless Integration with Discord**: Utilizes Discord for notifications, ensuring users and support teams receive timely updates and communications.

4. **Efficient Workflow Management**: Leverages Kestra for workflow orchestration, enabling efficient task automation and scheduling.

5. **User-Friendly Interface**: Provides an intuitive and easy-to-navigate interface, making it accessible for users of all technical levels.

6. **Scalable Architecture**: Built with Flask, allowing for easy scaling and deployment to accommodate growing user bases and feature expansions.

## 🛠️ Technologies Used

- **Flask**: A lightweight WSGI web application framework in Python.
- **Kestra**: A workflow orchestration tool used for managing and executing workflows.
- **Discord**: Used for sending notifications.
- **HTML/CSS**: For the frontend design.
- **Python**: For handling form submissions and API calls.

## 📂 Project Structure

- **Frontend**: Contains HTML and CSS files for the user interface.
- **Backend**: Flask application handling form submissions and API interactions.
- **Workflows**: Defined using Kestra for automating tasks like ticket classification and fitness routine scheduling.


## 📦 Installation

1. Clone the repository.
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Flask application:
   ```bash
   python app.py
   ```

## 🎯 API Endpoints

### Customer Support
- `POST /customer_support`: Submit a support ticket
  - Required fields: name, email, message

### Fitness Routine
- `POST /fitness-routine`: Get personalized fitness routine
  - Required fields: name, age, gender, body_weight, parts, location, fitness_level, discord_webhook

## 🔒 Security

- All API keys and sensitive data should be stored in environment variables
- Discord webhooks should be kept private
- HTTPS is required for production deployment

## 📈 Future Improvements

- [ ] Add user authentication
- [ ] Implement real-time chat support
- [ ] Add more fitness routine customization options
- [ ] Create mobile app version
- [ ] Integrate with more messaging platforms

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📧 Contact

For any inquiries, please contact us at [naymul504@gmail.com](mailto:naymul504@gmail.com).

---

Enjoy using the Event-Driven Customer Support & Fitness Routine Recommender! 🎉
