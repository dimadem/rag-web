

export default async function handler(req, res) {
    if (req.method === 'POST') {
        const { question } = req.body;

        const response = await fetch('http://3.68.186.140:8000/api/ask', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ question }),
        });

        const data = await response.json();
        res.status(200).json(data);
    } else {
        res.setHeader('Allow', ['POST']);
        res.status(405).end(`Method ${req.method} Not Allowed`);
    }
}