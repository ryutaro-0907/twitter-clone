import type { NextPage } from 'next';
import Head from 'next/head';
import { GetStaticProps, GetStaticPaths, GetServerSideProps } from 'next'

import { useDispatch, useSelector } from 'react-redux';

import Sidebar from '../components/Sidebar';
import Feed from '../components/Feed';
import Widgets from '../components/Widgets';
import { fetchTweets } from '../utils/tweet_handler';
import { Tweet } from '../typings';
import { Toaster } from 'react-hot-toast';
import { client } from '../utils/axios';
import { store } from '../redux/store'
import { userSlice } from '../redux/userSlice'

interface Props {
  tweets: Tweet[];
}

const Home = ({ tweets }: Props) => {
  console.log("tweets at Home", tweets)
  const dispatch = useDispatch();
  const { login, logout, setStateUsername } = userSlice.actions;
  const is_login = store.getState().user.is_login
  console.log('logged in=', is_login)

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
  const tweets: Tweet[] = await fetchTweets() as Tweet[];
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