"use client";

export default function ProfilePage() {
  return (
    <div className="w-full min-h-screen bg-gray-100 flex justify-center py-10">
      <div className="w-[900px] bg-white rounded-xl shadow-md p-8 border">
        
        <a href="/dashboard" className="text-blue-600 text-sm underline">
          ← Go back
        </a>

        <div className="mt-6 grid grid-cols-3 gap-6 border p-6 rounded-lg">
          
          {/* IMAGE */}
          <div>
            <img
              src="https://randomuser.me/api/portraits/women/44.jpg"
              alt="profile"
              className="rounded-lg w-full"
            />
          </div>

          {/* LEFT INFO */}
          <div className="col-span-1 flex flex-col gap-4">
            <div>
              <p className="text-gray-500 text-sm">Name</p>
              <p className="font-semibold text-gray-800">Nina Valentine</p>
            </div>

            <div>
              <p className="text-gray-500 text-sm">Job Title</p>
              <p className="font-semibold text-gray-800">Actress</p>
            </div>

            <div>
              <p className="text-gray-500 text-sm">Email</p>
              <p className="font-semibold text-blue-600">nina_val@example.com</p>
            </div>
          </div>

          {/* RIGHT INFO */}
          <div className="flex flex-col gap-4">
            <div>
              <p className="text-gray-500 text-sm">LinkedIn</p>
              <a href="#" className="text-blue-600">linkedin.com</a>
            </div>

            <div>
              <p className="text-gray-500 text-sm">Twitter</p>
              <a href="#" className="text-blue-600">x.com</a>
            </div>

            <div>
              <p className="text-gray-500 text-sm">Facebook</p>
              <a href="#" className="text-blue-600">facebook.com</a>
            </div>
          </div>

        </div>

        {/* BIO */}
        <div className="mt-6 border p-4 rounded-lg text-gray-700">
          <p className="font-semibold mb-2">Bio</p>
          <p>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent
            aliquet odio augue, in dapibus lacus imperdiet ut. Quisque
            elementum placerat neque rhoncus tempus.
          </p>
        </div>

        <div className="mt-4">
          <button className="text-blue-600 underline">Edit Profile</button>
        </div>
      </div>
    </div>
  );
}
