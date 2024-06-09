'use client';

import { useEffect, useRef, useState } from 'react';

type Role = 'user' | 'assistant';

interface Message {
    content: string;
    role: Role;
}


//todo scroll to bottom

const ChatUi = () => {
    const [messages, setMessages] = useState<Message[]>([]);
    const [input, setInput] = useState('');


    const messagesEndRef = useRef<HTMLDivElement | null>(null);

    useEffect(() => {
        messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
    }, [messages]);

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
        <div className='relative w-svw h-svh'>
            {/* bg */}
            <div className='absolute flex items-center justify-center -z-10 blur-sm w-full h-full'>
                <p className='text-9xl uppercase text-pretty break-words text-center'>
                    {input}
                </p>
            </div>
            {/* messages */}
            <div className='absolute z-0 w-full h-full'>
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
                            className="fixed bottom-0 w-[90%] max-w-md p-2 mb-8 border border-gray-300 rounded shadow-xl mx-4 text-black"
                            value={input}
                            placeholder="Say something..."
                            onChange={e => setInput(e.target.value)}
                        />
                        {/* <button className="fixed bottom-0 right-0 p-2 mb-8 mr-2 bg-gray-900 text-white rounded shadow-xl">
                    -&gt;&gt;
                </button> */}
                    </form>
                </div>
            </div>
        </div>
    );
};

export { ChatUi };