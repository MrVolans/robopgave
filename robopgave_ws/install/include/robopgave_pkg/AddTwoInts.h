// Generated by gencpp from file robopgave_pkg/AddTwoInts.msg
// DO NOT EDIT!


#ifndef ROBOPGAVE_PKG_MESSAGE_ADDTWOINTS_H
#define ROBOPGAVE_PKG_MESSAGE_ADDTWOINTS_H

#include <ros/service_traits.h>


#include <robopgave_pkg/AddTwoIntsRequest.h>
#include <robopgave_pkg/AddTwoIntsResponse.h>


namespace robopgave_pkg
{

struct AddTwoInts
{

typedef AddTwoIntsRequest Request;
typedef AddTwoIntsResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct AddTwoInts
} // namespace robopgave_pkg


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::robopgave_pkg::AddTwoInts > {
  static const char* value()
  {
    return "6a2e34150c00229791cc89ff309fff21";
  }

  static const char* value(const ::robopgave_pkg::AddTwoInts&) { return value(); }
};

template<>
struct DataType< ::robopgave_pkg::AddTwoInts > {
  static const char* value()
  {
    return "robopgave_pkg/AddTwoInts";
  }

  static const char* value(const ::robopgave_pkg::AddTwoInts&) { return value(); }
};


// service_traits::MD5Sum< ::robopgave_pkg::AddTwoIntsRequest> should match
// service_traits::MD5Sum< ::robopgave_pkg::AddTwoInts >
template<>
struct MD5Sum< ::robopgave_pkg::AddTwoIntsRequest>
{
  static const char* value()
  {
    return MD5Sum< ::robopgave_pkg::AddTwoInts >::value();
  }
  static const char* value(const ::robopgave_pkg::AddTwoIntsRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::robopgave_pkg::AddTwoIntsRequest> should match
// service_traits::DataType< ::robopgave_pkg::AddTwoInts >
template<>
struct DataType< ::robopgave_pkg::AddTwoIntsRequest>
{
  static const char* value()
  {
    return DataType< ::robopgave_pkg::AddTwoInts >::value();
  }
  static const char* value(const ::robopgave_pkg::AddTwoIntsRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::robopgave_pkg::AddTwoIntsResponse> should match
// service_traits::MD5Sum< ::robopgave_pkg::AddTwoInts >
template<>
struct MD5Sum< ::robopgave_pkg::AddTwoIntsResponse>
{
  static const char* value()
  {
    return MD5Sum< ::robopgave_pkg::AddTwoInts >::value();
  }
  static const char* value(const ::robopgave_pkg::AddTwoIntsResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::robopgave_pkg::AddTwoIntsResponse> should match
// service_traits::DataType< ::robopgave_pkg::AddTwoInts >
template<>
struct DataType< ::robopgave_pkg::AddTwoIntsResponse>
{
  static const char* value()
  {
    return DataType< ::robopgave_pkg::AddTwoInts >::value();
  }
  static const char* value(const ::robopgave_pkg::AddTwoIntsResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // ROBOPGAVE_PKG_MESSAGE_ADDTWOINTS_H