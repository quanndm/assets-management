import { FeatherIconName } from "../../common/types";

type Props = {
  nameIcon: FeatherIconName;
  className?: string;
  width?: number;
  height?: number;
};

const FeatherIcon = (props: Props) => {
  const { nameIcon, width, height, className } = props;

  return (
    <i
      data-feather={nameIcon}
      className={className}
      style={{ width, height }}
    />
  );
};

export default FeatherIcon;
