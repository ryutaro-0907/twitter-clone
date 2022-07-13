import NextAuth from "next-auth"
import GoogleProvider from "next-auth/providers/google"

// FIXME: can not use this with nginx.
export default NextAuth({
  // Configure one or more authentication providers
  providers: [
    GoogleProvider({
        clientId: process.env.GOOGLE_CLIENT_ID,
        clientSecret: process.env.GOOGLE_CLIENT_SECRET,
      }),
  ],
  callbacks: {
    async redirect() {
      // Allows relative callback URLs
      return 'http://0.0.0.0:3000/api/auth/callback/google'
    }
  }
})