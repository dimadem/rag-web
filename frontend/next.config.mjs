/** @type {import('next').NextConfig} */
const nextConfig = {
    async rewrites() {
        return [
            {
                source: '/api/:path*',
                destination: 'http://3.67.196.157:8000/api/:path*',
            }
        ];
    },
};

export default nextConfig;
