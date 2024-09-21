background = '''
I am a software engineer with 1.5 years of experience in backend development, specializing in Python. 
Throughout my career, I have worked in diverse environments, collaborating with experts across various domains. 
Starting from a point where I had little direction, I encountered both guided and self-driven learning. 
Over time, I realized the importance of making independent decisions, as they foster growth through firsthand experience, regardless of challenges.

My passion for becoming a software engineer was fueled by observing industry experts. 
Their accomplishments motivated me to pursue this career, and I quickly learned that continuous learning is essential in the IT industry. 
The rapid evolution of technology means that staying current is crucial for success. 
To achieve this, I actively engage with my professional network, keeping myself updated on the latest trends and innovations through personal projects and collaborations.

Entering the industry required persistence, applying to multiple companies and focusing on mid-level firms to gain exposure to experienced professionals. 
The transition from academia to professional life was eye-opening, but I adapted by following the advice of my mentors while exploring the industry independently. 
I firmly believe in the value of best practices, learning from seniors, and never hesitating to seek advice or collaborate on challenging tasks.

Currently, as a senior software engineer, I am committed to continuous learning and meeting project deadlines. 
I prioritize using efficient design patterns like the repository design pattern and dependency containers to maintain project architecture. 
I also ensure that my code is well-documented, sharing my knowledge with juniors to help them grow. 
By attending industry events and participating in expert communities, I stay informed about emerging technologies and remain competitive in my field.
'''



# article_title = '''
# Here's how you can enhance your problem-solving skills as a programmer.
# '''

# article_segment_head = '''
# Understand Basics
# '''

# article_segment_description = '''
# Before diving into complex problem-solving, ensure that you have a strong grasp of programming fundamentals. This includes understanding data structures like arrays, lists, and trees, as well as algorithms, which are step-by-step procedures for calculations. Familiarity with the basics allows you to recognize patterns and apply the right concepts when solving a problem. If you encounter a challenge, revisit the basics to reinforce your foundation, as this will make it easier to deconstruct and tackle more advanced issues.
# '''



def generate_prompt(background, article_title, article_segment_head, article_segment_description):

    joined_prompt = f'''
    ### USER BACKGROUND AND APPROACHES:
    {background}

    ### TASK:
    Write a concise, contributional comment on the article below, based on the user's background and approaches. The goal is to provide thoughtful, relevant input that aligns with the selected section of the article.

    ### ARTICLE INFORMATION:

    **Article Topic:**
    {article_title}

    **User Selected Section to Contribute:**
    - **Section Title:** {article_segment_head}
    - **Section Summary:** {article_segment_description}

    ### GUIDELINES:
    When writing the contribution, consider these points:
    1. Start by sharing the user's experience. (e.g., "In my experience...")
    2. Highlight one useful approach or insight. (e.g., "One thing I have found helpful is...")
    3. Provide a suggestion or applicable approach. (e.g., "What we can apply here is...")

    ### ADDITIONAL NOTES:
    - **Character Limit:** Maximum 750 characters.
    - **Tone:** Ensure the comment is conversational, informative, and professional.
    
    ### DESIRED OUTPUT:
    The output should be in JSON format with the following keys:
    - "result": The final comment based on the information provided.
    - "match_percentage": How closely the comment aligns with the user's background (expressed as a percentage).

    '''
    return joined_prompt