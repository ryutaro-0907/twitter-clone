# twitter-colne

# Set up

# Install direnv and crate .envrc file as follows
```
export GOOGLE_CLIENT_ID=
export GOOGLE_CLIENT_SECRET=

export NEXTAUTH_URL=http://localhost:3000/
<!-- any secret is fine. -->
export NEXTAUTH_SECRET=codeforfun

export NEXT_PUBLIC_SANITY_DATASET=production
export NEXT_PUBLIC_SANITY_PROJECT_ID=
export NEXT_PUBLIC_BASE_URL=http://localhost:3000/
export SANITY_API_TOKEN=
```

## Note:
You need to have an access to Sanity and google API to use some backend processes.

# After you set up
Run
```
npm install
npm run dev
```