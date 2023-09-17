const { OpenAI } = require("openai");

require('dotenv').config();

async function generateText() {
    const openai = new OpenAI({
        apiKey: process.env.OPENAI_API_KEY,
    });

    try {
        const chatCompletion = await openai.chat.completions.create({
            messages: [{ role: "user", content: "I am going to give you a prompt that resembles a math equation in Latex. This expression has been parsed to integrate with Wolfram Alpha. Respond with the the highest probability answer. Do not invent math that is impossible."}],
            model: "gpt-3.5-turbo",
        });
        console.log(chatCompletion);
        console.log(chatCompletion.choices[0].message)
    } catch (error) {
        console.error("Error:", error.response ? error.response.data : error.message);
    }
}

generateText();
