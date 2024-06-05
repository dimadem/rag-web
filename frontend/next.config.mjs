/** @type {import('next').NextConfig} */
const nextConfig = {
    async rewrites() {
        return [
            {
                source: '/api/:path*',
                destination: 'http://52.57.91.70:8000/api/:path*',
            }
        ];
    },
};

export default nextConfig;
