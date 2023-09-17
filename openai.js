const { OpenAI } = require("openai");

require('dotenv').config();

async function generateText() {
    const openai = new OpenAI({
        apiKey: process.env.OPENAI_API_KEY,
    });

    try {
        const chatCompletion = await openai.chat.completions.create({
            messages: [{ role: "user", content: "I am going to give you text as if I was writing notes in a 6.006 MIT class. Respond with the three highest probability continuations, and rank them. Binary search is O(log(n)) because"}],
            model: "gpt-3.5-turbo",
        });
        console.log(chatCompletion);
        console.log(chatCompletion.choices[0].message)
    } catch (error) {
        console.error("Error:", error.response ? error.response.data : error.message);
    }
}

generateText();
