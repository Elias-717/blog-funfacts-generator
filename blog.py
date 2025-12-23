from google import genai
from dotenv import load_dotenv
import os


# Loading the key variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in environment variables!")

client = genai.Client(api_key=api_key)  

# Function to generate blog content
def generate_blog(title):
    prompt = (
        f"write fun facts as a blog style that is engaging. it must be about:\n\n{title}\n\n"
        "Make sure it is only around 100 words long, "
        "make it fun and interesting to read."
        "make sure it does not sound like an ai wrote it."
        "use dark humor and make it very engaging."
    )
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )
    return response.text.strip()

# Main execution
if __name__ == "__main__":
    blog_title = input("Type the blog title: ")
    blog_post = generate_blog(blog_title)
    
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>{blog_title}</title>
        <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
        <style>
            * {{ margin: 0; padding: 0; box-sizing: border-box; }}

            body {{
                font-family: 'Roboto', sans-serif;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                background: url('blog_background.jpeg') no-repeat center center fixed;
                background-size: cover;
                color: #fff;
                text-align: center;
                padding: 20px;
            }}

            .hero-card {{
                background: rgba(0,0,0,0.7);
                backdrop-filter: blur(12px);
                border-radius: 25px;
                padding: 60px 40px;
                max-width: 1000px;
                width: 90%;
                box-shadow: 0 20px 50px rgba(0,0,0,0.6);
                position: relative;
                overflow: hidden;
                animation: fadeIn 1s ease forwards;
            }}

            h1 {{
                font-size: 4rem;
                font-weight: 700;
                margin-bottom: 40px;
                text-shadow: 3px 3px 15px rgba(0,0,0,0.7);
            }}

            p {{
                font-size: 1.8rem;
                line-height: 1.8;
                text-shadow: 2px 2px 10px rgba(0,0,0,0.6);
            }}

            /* Floating decorative shapes */
            .shape {{
                position: absolute;
                border-radius: 50%;
                opacity: 0.2;
                animation: float 12s ease-in-out infinite;
            }}
            .shape1 {{ width: 120px; height: 120px; background: #ff5722; top: -60px; left: -60px; }}
            .shape2 {{ width: 150px; height: 150px; background: #00bcd4; bottom: -80px; right: -80px; }}
            .shape3 {{ width: 80px; height: 80px; background: #ffeb3b; top: 25%; right: -40px; }}

            @keyframes float {{
                0%, 100% {{ transform: translateY(0) translateX(0); }}
                50% {{ transform: translateY(-20px) translateX(20px); }}
            }}

            @keyframes fadeIn {{
                0% {{ opacity: 0; transform: translateY(20px); }}
                100% {{ opacity: 1; transform: translateY(0); }}
            }}

            @media (max-width: 768px) {{
                h1 {{ font-size: 3rem; }}
                p {{ font-size: 1.2rem; }}
                .hero-card {{ padding: 40px 20px; }}
            }}
        </style>
    </head>
    <body>
        <div class="hero-card">
            <h1>{blog_title}</h1>
            <p>{blog_post}</p>

            <!-- Floating shapes -->
            <div class="shape shape1"></div>
            <div class="shape shape2"></div>
            <div class="shape shape3"></div>
        </div>
    </body>
    </html>
    """

    
blog_file_path = os.path.join(os.path.dirname(__file__), "index.html")

# Write/overwrite the HTML
with open(blog_file_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Blog generated successfully! Overwritten at {blog_file_path}")
