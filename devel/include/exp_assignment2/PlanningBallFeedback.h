// Generated by gencpp from file exp_assignment2/PlanningBallFeedback.msg
// DO NOT EDIT!


#ifndef EXP_ASSIGNMENT2_MESSAGE_PLANNINGBALLFEEDBACK_H
#define EXP_ASSIGNMENT2_MESSAGE_PLANNINGBALLFEEDBACK_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <geometry_msgs/Pose.h>

namespace exp_assignment2
{
template <class ContainerAllocator>
struct PlanningBallFeedback_
{
  typedef PlanningBallFeedback_<ContainerAllocator> Type;

  PlanningBallFeedback_()
    : stat()
    , position()  {
    }
  PlanningBallFeedback_(const ContainerAllocator& _alloc)
    : stat(_alloc)
    , position(_alloc)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _stat_type;
  _stat_type stat;

   typedef  ::geometry_msgs::Pose_<ContainerAllocator>  _position_type;
  _position_type position;





  typedef boost::shared_ptr< ::exp_assignment2::PlanningBallFeedback_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::exp_assignment2::PlanningBallFeedback_<ContainerAllocator> const> ConstPtr;

}; // struct PlanningBallFeedback_

typedef ::exp_assignment2::PlanningBallFeedback_<std::allocator<void> > PlanningBallFeedback;

typedef boost::shared_ptr< ::exp_assignment2::PlanningBallFeedback > PlanningBallFeedbackPtr;
typedef boost::shared_ptr< ::exp_assignment2::PlanningBallFeedback const> PlanningBallFeedbackConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::exp_assignment2::PlanningBallFeedback_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::exp_assignment2::PlanningBallFeedback_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace exp_assignment2

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'geometry_msgs': ['/opt/ros/kinetic/share/geometry_msgs/cmake/../msg'], 'actionlib_msgs': ['/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg'], 'exp_assignment2': ['/home/sabrino/exprob/Assignment2-Experimental-RoboticS-LAB/src/exp_assignment2/msg', '/home/sabrino/exprob/Assignment2-Experimental-RoboticS-LAB/devel/share/exp_assignment2/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::exp_assignment2::PlanningBallFeedback_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::exp_assignment2::PlanningBallFeedback_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::exp_assignment2::PlanningBallFeedback_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::exp_assignment2::PlanningBallFeedback_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::exp_assignment2::PlanningBallFeedback_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::exp_assignment2::PlanningBallFeedback_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::exp_assignment2::PlanningBallFeedback_<ContainerAllocator> >
{
  static const char* value()
  {
    return "436d418e7944afa3067a7cb1612a2ab0";
  }

  static const char* value(const ::exp_assignment2::PlanningBallFeedback_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x436d418e7944afa3ULL;
  static const uint64_t static_value2 = 0x067a7cb1612a2ab0ULL;
};

template<class ContainerAllocator>
struct DataType< ::exp_assignment2::PlanningBallFeedback_<ContainerAllocator> >
{
  static const char* value()
  {
    return "exp_assignment2/PlanningBallFeedback";
  }

  static const char* value(const ::exp_assignment2::PlanningBallFeedback_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::exp_assignment2::PlanningBallFeedback_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
string stat\n\
geometry_msgs/Pose position\n\
\n\
\n\
================================================================================\n\
MSG: geometry_msgs/Pose\n\
# A representation of pose in free space, composed of position and orientation. \n\
Point position\n\
Quaternion orientation\n\
\n\
================================================================================\n\
MSG: geometry_msgs/Point\n\
# This contains the position of a point in free space\n\
float64 x\n\
float64 y\n\
float64 z\n\
\n\
================================================================================\n\
MSG: geometry_msgs/Quaternion\n\
# This represents an orientation in free space in quaternion form.\n\
\n\
float64 x\n\
float64 y\n\
float64 z\n\
float64 w\n\
";
  }

  static const char* value(const ::exp_assignment2::PlanningBallFeedback_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::exp_assignment2::PlanningBallFeedback_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.stat);
      stream.next(m.position);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct PlanningBallFeedback_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::exp_assignment2::PlanningBallFeedback_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::exp_assignment2::PlanningBallFeedback_<ContainerAllocator>& v)
  {
    s << indent << "stat: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.stat);
    s << indent << "position: ";
    s << std::endl;
    Printer< ::geometry_msgs::Pose_<ContainerAllocator> >::stream(s, indent + "  ", v.position);
  }
};

} // namespace message_operations
} // namespace ros

#endif // EXP_ASSIGNMENT2_MESSAGE_PLANNINGBALLFEEDBACK_H
