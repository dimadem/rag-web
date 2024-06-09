'use client';

import { useEffect, useRef, useState } from 'react';
import { Input } from '@/shared/components/ui/input';
import { Button } from '@/shared/components/ui/button';
import { ScrollArea } from '@/shared/components/ui/scroll-area';
import { Separator } from '@/shared/components/ui/separator';
import { Badge } from '@/shared/components/ui/badge';
import { Tooltip, TooltipContent, TooltipProvider, TooltipTrigger } from '@/shared/components/ui/tooltip';

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

        const newMessages: Message[] = [...messages, { content: input, role: 'user' }];

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

        setMessages([...newMessages, { role: 'assistant', content: data.response }]);
    };

    return (
        <div className="relative h-svh w-svw">
            {/* bg */}
            <div className="absolute -z-10 flex h-full w-full items-center justify-center blur-sm">
                <p className="text-pretty break-words text-center text-9xl">{input}</p>
            </div>
            <nav className="flex flex-row items-center gap-5 text-sm">
                <p className='mx-auto my-2 text-xl'>RAG & WIKI</p>
            </nav>
            {/* messages */}
            <div className="absolute z-0 h-full w-full">
                <div className="stretch mx-auto flex w-full max-w-md flex-col h-full">
                    <ScrollArea className="flex-1 rounded-md border p-4 mx-2 h-full mb-32">
                        {messages.map((m, i: number) => (
                            <div
                                key={i}
                                className="relative whitespace-pre-wrap p-1">
                                <br />
                                <Badge className='text-pretty flex items-end justify-end w-fit ml-auto'>
                                    {m.role === 'user' ? 'USER' : ' AI '}
                                </Badge>
                                <br />
                                {m.content}
                                <br />
                                <br />
                                <Separator />
                            </div>
                        ))}
                    </ScrollArea>
                    <form
                        onSubmit={handleSubmit}
                        className='fixed bottom-0 mb-8 flex w-svw sm:max-w-md items-center justify-between space-x-2 px-2'>
                        <Input
                            type="text"
                            value={input}
                            placeholder="Write Wikipedia title"
                            onChange={(e) => setInput(e.target.value)}
                        />
                        <Button type='submit'>send</Button>
                    </form>
                </div>
            </div >
        </div >
    );
};

export { ChatUi };
