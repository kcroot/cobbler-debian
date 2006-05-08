"""
Messages used by cobbler.
This module encapsulates strings so they can
be reused and potentially translated.

Michael DeHaan <mdehaan@redhat.com>
"""

_msg_table = {
  "bad_server"      : "server field in /var/lib/cobbler/settings must be set to something other than localhost, or kickstarts will fail",
  "parse_error"     : "could not read %s, replacing...",
  "no_create"       : "cannot create: %s",
  "no_args"         : "this command requires arguments.",
  "missing_options" : "cannot add, all parameters have not been set",
  "unknown_cmd"     : "cobbler doesn't understand '%s'",
  "bad_arg"         : "expecting an equal sign in argument '%s'",
  "reject_arg"      : "the value of parameter '%s' is not valid",
  "weird_arg"       : "this command doesn't take a parameter named '%s'",
  "bad_sys_name"    : "system name must be a MAC, IP, or resolveable host",
  "usage"           : "for help, see 'man cobbler'",
  "need_to_fix"     : "the following potential problems were detected:",
  "need_perms"      : "cobbler cannot access %s",
  "no_dhcpd"        : "can't find dhcpd, try 'yum install dhcpd'",
  "no_pxelinux"     : "can't find pxelinux, try 'yum install pxelinux'",
  "no_tftpd"        : "can't find tftpd, try 'yum install tftpd'",
  "no_dir"          : "can't find %s, need to create it",
  "chg_attrib"      : "need to change '%s' to '%s' in '%s'",
  "no_exist"        : "%s does not exist",
  "no_line"         : "file '%s' should have a line '%s' somewhere",
  "no_dir2"         : "can't find %s for %s as referenced in /var/lib/cobbler/settings",
  "no_cfg"          : "could not find a valid /var/lib/cobbler/settings, rebuilding",
  "bad_param"       : "at least one parameter is missing for this function",
  "empty_list"      : "(Empty)",
  "err_resolv"      : "system (%s) did not resolve",
  "err_kickstart"   : "kickstart (%s) for item (%s) is not valid",
  "err_kickstart2"  : "error mirroring kickstart file (%s) to (%s)",
  "orphan_profile2" : "system references a non-existant profile",
  "orphan_system2"  : "system does not reference a profile",
  "orphan_profile"  : "removing this distro would break a profile",
  "orphan_system"   : "removing this profile would break a system",
  "delete_nothing"  : "can't delete something that doesn't exist",
  "no_distro"       : "distro does not exist",
  "no_profile"      : "profile does not exist",
  "no_kickstart"    : "kickstart must be an http://, ftp:// or nfs:// URL",
  "no_kernel"       : "the kernel needs to be a directory containing a kernel, or a full path.  Kernels must be named just 'vmlinuz' or in the form 'vmlinuz-AA.BB.CC-something'",
  "sync_kernel"     : "the kernel (%s) for distro (%s) cannot be found and must be fixed",
  "sync_initrd"     : "the initrd (%s) for distro (%s) cannot be found and must be fixed",
  "sync_mirror_ks"  : "mirroring local kickstarts...",
  "sync_buildtree"  : "building trees",
  "sync_processing" : "processing: %s",
  "writing"         : "writing file: %s",
  "mkdir"           : "creating: %s",
  "dryrun"          : "dry run | %s",
  "copying"         : "copying file: %s to %s",
  "removing"        : "removing: %s",
  "no_initrd"       : "the initrd needs to be a directory containing an initrd, or a full path.  Initrds must be named just 'initrd.img' or in the form 'initrd-AA.BB.CC-something.img",
  "check_ok"        : """
No setup problems found.

Manual editing of /var/lib/cobbler/settings and dhcpd.conf is suggested to tailor them to your specific configuration.  Furthermore, it's important to know that cobbler can't completely understnad what you intend to do with dhcpd.conf, but it looks like there is at least some PXE related information in it.  We'll leave this up to you.

Good luck.
""",
  "help"           : "see 'man cobbler'"
}

def lookup(key):
   """
   Return the lookup of a string key.
   """
   if _msg_table.has_key(key):
       return _msg_table[key]
   else:
       return key
