/** @type {import('next').NextConfig} */
const nextConfig = {
    async rewrites() {
        return [
            {
                source: '/api/:path*',
                destination: 'http://3.68.186.140:8000/api/:path*',
            }
        ];
    },
};

export default nextConfig;
