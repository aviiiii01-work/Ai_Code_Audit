const mongoose = require("mongoose");

const productSchema = new mongoose.Schema(
  {
    title: { type: String, trim: true, required: true },
    price: { type: Number, required: true },
    rating: { type: Number, default: 0 },
    status: { type: String, enum: ["active", "archived"], default: "active" },
    deletedAt: { type: Date, default: null }
  },
  { timestamps: true }
);

productSchema.virtual("formattedPrice").get(function () {
  return `₹${this.price.toFixed(2)}`;
});

productSchema.index({ status: 1, createdAt: -1 });

module.exports = mongoose.model("Product", productSchema);
