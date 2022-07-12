import type { NextPage } from 'next';
import Head from 'next/head';
import Image from 'next/image';
import { GetStaticProps, GetStaticPaths, GetServerSideProps } from 'next'

import Sidebar from '../components/Sidebar';
import Feed from '../components/Feed';
import Widgets from '../components/Widgets';
import { fetchTweets } from '../utils/fetchTweets';
import { Tweet } from '../typings';
import { Toaster } from 'react-hot-toast';

interface Props {
  tweets: Tweet[];
}

const test = async () => {
  try {
    const data = await fetch('http://nginx:8080/api/tweets')
    const tweets: Tweet[] = await data.json()
    console.log(tweets)
    return tweets
  } catch (err) {
    console.error(err) //
}}

const Home = ({ tweets }: Props) => {
  console.log("tweets at Home", tweets)
  test()
  return (
    <div className="mx-auto max-h-screen overflow-hidden lg:max-w-6xl">
      <Head>
        <title>Twitter With Python & Next.js</title>
      </Head>
      <Toaster />
      <main className="grid grid-cols-9">
        <Sidebar/>

        <Feed tweets={tweets} />

        <Widgets/>
      </main>
    </div>
  )
}

export default Home;


export const getServerSideProps: GetServerSideProps = async () => {
  // const tweets: Tweet[] = await (await fetch('http://nginx:8080/api/tweets')).json()
  const tweets: Tweet[] = await test() as Tweet[];
  console.log(tweets)
  return {
    props: {
      tweets: tweets
    }
  }
}

// export const getServerSideProps: GetServerSideProps = async () => {
//   console.log("getServerSideProps called  with server side properties");
//   try {
//     const tweets = await fetchTweets();
//     console.log(`tweets at getServerSideProps: ${tweets}`)
//     if (tweets.length != 0) {
//       return {
//         props: {
//           tweets,
//         }
//       }
//     } else {
//       const returnNull = 'tweet not found'
//       console.error("tweets not found: fetchTweets failed to return tweets.")

//       return {
//         props: {
//           returnNull,
//         }
//       }
//     }
//   } catch (err) {
//       const dummies = []
//       const dummy = {
//         id: 0,
//         created_at: 'string',
//         user_id: 0,
//         text: 'failed to fetch tweet at getServerSideProps. ',
//         username: 'string',
//         profile_image: 'string',
//         images: 'string',

//       } as Tweet;
//       dummies.push(dummy)
//     return {
//       props: {
//         dummies,
//       }
//     }
//   }

// }