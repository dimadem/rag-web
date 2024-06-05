'use client';

import { useState } from 'react';

type Message = {
    role: 'user' | 'assistant';
    content: string;
};

//!fix types 

const ChatUi = () => {
    const [messages, setMessages] = useState<Message[]>([]);
    const [input, setInput] = useState('');

    const handleSubmit = async (e: any) => {
        e.preventDefault();

        const newMessages = [
            ...messages,
            { content: input, role: 'user' },
        ];

        setMessages(newMessages);
        setInput('');

        const response = await fetch('/api/ask', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ question: input }),
        });

        const data = await response.json();

        setMessages([
            ...newMessages,
            { role: 'assistant', content: data.response },
        ]);
    };

    return (
        <div className="flex flex-col w-full h-screen max-w-md py-24 mx-auto stretch">
            {messages.map((m, i: number) => (
                <div key={i} className="whitespace-pre-wrap">
                    {m.role === 'user' ? 'User: ' : 'AI: '}
                    {m.content}
                </div>
            ))}

            <form onSubmit={handleSubmit}>
                <input
                    className="fixed bottom-0 w-full max-w-md p-2 mb-8 border border-gray-300 rounded shadow-xl"
                    value={input}
                    placeholder="Say something..."
                    onChange={e => setInput(e.target.value)}
                />
            </form>
        </div>
    );
};

export { ChatUi };