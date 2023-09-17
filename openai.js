const { OpenAI } = require("openai");

require('dotenv').config();

/*const openai = new OpenAI({
    apiKey: process.env.OPENAI_API_KEY,
});

const chatCompletion = await openai.chat.completions.create({
    messages: [{ role: "user", content: "Say this is a test" }],
    model: "gpt-3.5-turbo",
});*/

async function generateText() {
    const openai = new OpenAI({
        apiKey: process.env.OPENAI_API_KEY,
    });

    try {
        const chatCompletion = await openai.chat.completions.create({
            messages: [{ role: "user", content: "Say this is a test" }],
            model: "gpt-3.5-turbo",
        });
        console.log(chatCompletion);
        console.log(chatCompletion.choices[0].message)
    } catch (error) {
        console.error("Error:", error.response ? error.response.data : error.message);
    }
}

generateText();
