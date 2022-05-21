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
const Home = ({ tweets }: Props) => {
  console.log("tweets", tweets)
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

export default Home

export const getServerSideProps: GetServerSideProps = async (context) => {
  try {
    const tweets = await fetchTweets();
    console.log(`tweets: ${tweets}`)
    if (tweets.length != 0) {
      return {
        props: {
          tweets,
        }
      }
    } else {
      const returnNull = null
      console.error("tweets not found: fetchTweets failed to return tweets.")

      return {
        props: {
          returnNull,
        }
      }
    }
  } catch (err) {
    console.log(err)
    const tweets = null;
    console.log("fetchTweets failed.")
    return {
      props: {
        tweets,
      }
    }
  }

}