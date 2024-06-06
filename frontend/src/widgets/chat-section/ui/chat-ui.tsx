'use client';

import { useState } from 'react';

type Role = 'user' | 'assistant';

interface Message {
    content: string;
    role: Role;
}

const ChatUi = () => {
    const [messages, setMessages] = useState<Message[]>([]);
    const [input, setInput] = useState('');

    const handleSubmit = async (e: any) => {
        e.preventDefault();

        const newMessages: Message[] = [
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
        <div className="flex flex-col w-full h-svh max-w-md py-24 mx-auto stretch">
            <div className='overflow-auto max-h-svh mx-4'>
                {messages.map((m, i: number) => (
                    <div key={i} className="whitespace-pre-wrap p-1">
                        <span className='font-bold uppercase'>
                            {m.role === 'user' ? 'USER -> ' : 'AI   -> '}
                        </span>
                        {m.content}
                    </div>
                ))}
            </div>
            <form onSubmit={handleSubmit}>
                <input
                    className="fixed bottom-0 w-[90%] max-w-md p-2 mb-8 border border-gray-300 rounded shadow-xl mx-4"
                    value={input}
                    placeholder="Say something..."
                    onChange={e => setInput(e.target.value)}
                />
                {/* <button className="fixed bottom-0 right-0 p-2 mb-8 mr-2 bg-gray-900 text-white rounded shadow-xl">
                    -&gt;&gt;
                </button> */}
            </form>
        </div>
    );
};

export { ChatUi };