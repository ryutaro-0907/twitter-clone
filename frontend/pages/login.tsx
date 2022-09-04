import { useState, useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { useRouter } from 'next/router'

import { userSlice } from '../redux/userSlice';
import { store } from '../redux/store';

interface UserLogin {
    email: string;
    password: string;
}

function login() {
    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')

    const router = useRouter()

    const dispatch = useDispatch();
    const { login, setStateUsername, setStateEmail } = userSlice.actions;

    const userLogin = async (e) => {
        e.preventDefault();

        const userLogin: UserLogin = {
            email: email,
            password: password,
        }

        const res  = fetch('http://localhost:8080/server/users/login', {
            body: JSON.stringify(userLogin),
            method: 'POST',
            headers: {
                'Content-type': 'application/json',
              },

        }).then(response => {
            const data = response.json()

            dispatch(login())
            dispatch(setStateEmail(email))
            dispatch(setStateUsername('afdsfsaf'))

            router.push('/')

        }).catch(() => alert('Email is already taken, please login'))
    }

    return (
      <div>
          <div className="bg-grey-lighter min-h-screen flex flex-col">
              <div className="container max-w-sm mx-auto flex-1
              flex flex-col items-center justify-center px-2">
                  <div className="bg-white px-6 py-8 rounded shadow-md text-black w-full">
                  <h1 className="mb-8 text3xl text-center">Log in</h1>
                  <form className="">
                      <input
                          value={email}
                          onChange={e => setEmail(e.target.value)}
                          type="text"
                          className="block border border-grey-light w-full p-3 rounded mb-4"
                          name="email"
                          placeholder="Email Address"
                           />
                      <input
                          value={password}
                          onChange={e => setPassword(e.target.value)}
                          type="password"
                          className="block border border-gray-light w-full p-3 rounded mb-4"
                          name="password"
                          placeholder="Password"
                           />
                      <button
                          type="submit"
                          disabled={!email || !password}
                          onClick={userLogin}
                          className="w-full text-center py-3 rounded
                           bg-blue-500 text-white
                           hober:bg-blue-200 focus:outline-none my-1">
                             Log in
                      </button>
                  </form>
                  </div>
                  <div className="text-grey-dark mt-6">
                      Don't have an account?
                      <a className="no-underline border-b border-blue text-blue-600" href="../signup"> Sign up!</a>
                  </div>
              </div>
          </div>
      </div>
    )
  }

  export default login