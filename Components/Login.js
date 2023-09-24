import React from 'react'
import Image from 'next/image';
import student from '../public/Reading-student.svg';
import pramukhClass from '../public/Pramukh_Classes.png';
import personLogo from '../public/person.svg';
import keyLogo from '../public/key.svg';
import authLogo from '../public/auth-logo.svg';
import './Login.css'


function Login() {
  return (
    <div className='flex justify-center items-center content-center'>
      {/*Inner Box for Login form*/}
      <div className='flex-col bg-white rounded-[20px] justify-center shadow-[0_-1px_18px_5px_rgba(0,0,0,0.25)]'>
        <div className='flex justify-center'>
          <Image
          width="200"
          alt="Comapany Logo"
          src={pramukhClass} />
        </div>
        <div className='bg-black h-[0.5px] text-sm mx-5'></div>

        <div className='flex-col'>

          {/*Username*/}
          <div className='mx-5 my-5 flex border-2  border-gray-200 rounded-[10px] w-[300px] h-[40px] '>
            <Image alt='person' src={personLogo} />
            <input className='outline-none'  type='text' placeholder='Username' />
          </div>

          {/*Password*/}
          <div className='mx-5 my-5 flex border-2 border-gray-200 rounded-[10px] w-[300px] h-[40px]'>
            <Image alt='person' src={keyLogo} />
            <input type='password' className='outline-none' placeholder='Password' />
          </div>

          {/*Forgot Password*/}
          <div className='mx-5 my-5 flex justify-center text-slate-600/70'>
            <p className='text-sm font-medium'>Forgot Password? <b className='text-blue-400'>Click Here!!</b></p>
          </div>
          {/*Login button */}
          <div className='mx-5 my-5 px-5 justify-center items-center bg-blue-600 flex text-white rounded-[10px] w-[300px] h-[40px]'>
          <Image alt='person' src={authLogo} className='h-7' />
            <button className=''>Login</button>
          </div>
        </div>
      </div>

      {/*Reading Student Image */}

      <div>
        <Image
        width="400"
        priority
        alt="student"
        src={student} />
      </div>


    </div>
  )
}

export default Login