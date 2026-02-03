require('dotenv').config({ path: '.env.local' });
const mongoose = require('mongoose');

console.log("MONGO_URI:", process.env.MONGO_URI);

mongoose.connect(process.env.MONGO_URI)
.then(() => console.log("✅ MongoDB connected"))
.catch(err => console.error("❌ MongoDB connection failed:", err));
