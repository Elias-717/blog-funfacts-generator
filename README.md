# Blog Fun Facts Generator

A fun and engaging blog generator that creates witty, dark humor-infused fun facts using Google's Gemini AI API.

## 📋 Description

This project automatically generates entertaining blog posts with fun facts about any topic. The generator uses the Google Gemini API to create engaging, humorous content (around 100 words) and dynamically generates a beautiful HTML page with a styled background to display the content.

## ✨ Features

- **AI-Powered Content Generation**: Uses Google Gemini 2.5 Flash model to create engaging blog posts
- **Dark Humor**: Generates content with dark humor and witty writing style
- **Dynamic HTML Generation**: Automatically creates styled HTML pages for each generated blog
- **Beautiful UI**: Includes animated decorative elements and a professional dark theme with background image
- **Responsive Design**: Adapts to different screen sizes

## 🛠️ Technologies Used

- **Python 3.x**
- **Google Gemini API** - for AI-powered content generation
- **HTML5 & CSS3** - for frontend
- **python-dotenv** - for environment variable management

## 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/blog-funfacts-generator.git
   cd blog-funfacts-generator
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   - Create a `.env` file in the project root
   - Add your Google Gemini API key:
     ```
     GEMINI_API_KEY=your_api_key_here
     ```
   - Get your API key from [Google AI Studio](https://aistudio.google.com/)

## 🚀 Usage

Run the script from the command line:

```bash
python blog.py
```

When prompted, enter the title or topic for your blog post:
```
Type the blog title: Your Topic Here
```

The script will:
1. Generate an engaging blog post using the Gemini API
2. Create a styled HTML file (`blog.html`) with the generated content
3. Display the result with a beautiful background image

## 📁 Project Structure

```
blog-funfacts-generator/
├── blog.py                 # Main Python script
├── blog.html              # Generated HTML output
├── blog_background.jpeg   # Background image for the blog
├── .env                   # Environment variables (not in repo)
├── .gitignore             # Git ignore file
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## 📋 Requirements

- Python 3.7 or higher
- Google Gemini API key
- Internet connection (for API calls)

## ⚙️ Configuration

The generated blogs include:
- **Length**: Approximately 100 words
- **Style**: Engaging with dark humor
- **Model**: Google Gemini 2.5 Flash
- **UI Theme**: Dark mode with animated decorative shapes

## 🔐 Security Notes

- **Never commit the `.env` file** to version control
- Keep your `GEMINI_API_KEY` private and secure
- Use environment variables instead of hardcoding sensitive information

## 📝 Example Output

The generator creates a beautiful HTML page with:
- Large, bold title
- Engaging blog content with dark humor
- Animated decorative shapes
- Fixed background image
- Responsive design for mobile and desktop

## 🤝 Contributing

Feel free to fork this repository and submit pull requests for any improvements!

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

Elias Sumairi

## 📞 Support

For issues or questions, please open an issue on the GitHub repository.

---

**Enjoy generating fun facts with AI!** 🎉
