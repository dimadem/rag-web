'use server';

import { createStreamableValue } from 'ai/rsc';
import { CoreMessage, streamText } from 'ai';
import { openai } from '@ai-sdk/openai';

async function continueConversation(messages: CoreMessage[]) {
    const result = await streamText({
        model: openai('gpt-4-turbo'),
        messages,
    });

    const stream = createStreamableValue(result.textStream);
    return stream.value;
}

export { continueConversation }