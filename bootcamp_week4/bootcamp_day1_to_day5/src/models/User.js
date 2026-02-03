const mongoose = require("mongoose");
const bcrypt = require("bcryptjs");
const validator = require("validator");

const userSchema = new mongoose.Schema(
  {
    firstName: { type: String, trim: true, required: true },
    lastName: { type: String, trim: true, required: true },
    email: {
      type: String,
      unique: true,
      lowercase: true,
      required: true,
      validate: value => validator.isEmail(value)
    },
    password: { type: String, minlength: 6, required: true },
    status: { type: String, enum: ["active", "inactive"], default: "active" }
  },
  { timestamps: true }
);

userSchema.virtual("fullName").get(function () {
  return `${this.firstName} ${this.lastName}`;
});

userSchema.pre("save", async function () {
  if (!this.isModified("password")) return;
  this.password = await bcrypt.hash(this.password, 10);
});

userSchema.index({ status: 1, createdAt: -1 });

module.exports = mongoose.model("User", userSchema);
