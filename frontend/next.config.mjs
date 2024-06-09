/** @type {import('next').NextConfig} */
const nextConfig = {
    async rewrites() {
        return [
            {
                source: '/api/:path*',
                destination: 'http://13.40.101.158:8000/api/:path*',
            }
        ];
    },
};

export default nextConfig;
