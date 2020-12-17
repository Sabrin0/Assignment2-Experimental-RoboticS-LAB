// Auto-generated. Do not edit!

// (in-package exp_assignment2.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class BallState {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.BallDetected = null;
      this.currentRadius = null;
    }
    else {
      if (initObj.hasOwnProperty('BallDetected')) {
        this.BallDetected = initObj.BallDetected
      }
      else {
        this.BallDetected = false;
      }
      if (initObj.hasOwnProperty('currentRadius')) {
        this.currentRadius = initObj.currentRadius
      }
      else {
        this.currentRadius = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type BallState
    // Serialize message field [BallDetected]
    bufferOffset = _serializer.bool(obj.BallDetected, buffer, bufferOffset);
    // Serialize message field [currentRadius]
    bufferOffset = _serializer.float64(obj.currentRadius, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type BallState
    let len;
    let data = new BallState(null);
    // Deserialize message field [BallDetected]
    data.BallDetected = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [currentRadius]
    data.currentRadius = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 9;
  }

  static datatype() {
    // Returns string type for a message object
    return 'exp_assignment2/BallState';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '5ead8a4581df1f9430fd7170d4a41e9e';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    bool BallDetected
    float64 currentRadius
    
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new BallState(null);
    if (msg.BallDetected !== undefined) {
      resolved.BallDetected = msg.BallDetected;
    }
    else {
      resolved.BallDetected = false
    }

    if (msg.currentRadius !== undefined) {
      resolved.currentRadius = msg.currentRadius;
    }
    else {
      resolved.currentRadius = 0.0
    }

    return resolved;
    }
};

module.exports = BallState;
